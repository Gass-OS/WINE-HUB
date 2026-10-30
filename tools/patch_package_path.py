import io, os, subprocess, sys, tarfile

OLD = b"/data/data/com.winlator"
NEW = b"/data/data/com.gass.hub"
assert len(OLD) == len(NEW)
OLDS, NEWS = OLD.decode(), NEW.decode()

def drain(dec):
    while dec.stdout.read(1 << 20):
        pass
    dec.stdout.close()
    if dec.wait() != 0:
        raise SystemExit("zstd decompress failed")

def scan(path):
    dec = subprocess.Popen(["zstd", "-dc", path], stdout=subprocess.PIPE)
    n = 0
    with tarfile.open(fileobj=dec.stdout, mode="r|") as tar:
        for m in tar:
            if m.issym() or m.islnk():
                if OLDS in m.linkname:
                    n += 1
            elif m.isreg():
                n += tar.extractfile(m).read().count(OLD)
    drain(dec)
    return n

def rewrite(path):
    tmp = path + ".new"
    dec = subprocess.Popen(["zstd", "-dc", path], stdout=subprocess.PIPE)
    enc = subprocess.Popen(["zstd", "-19", "-T0", "-q", "-f", "-o", tmp], stdin=subprocess.PIPE)
    n = 0
    with tarfile.open(fileobj=dec.stdout, mode="r|") as src, \
         tarfile.open(fileobj=enc.stdin, mode="w|", format=tarfile.GNU_FORMAT) as dst:
        for m in src:
            if m.issym() or m.islnk():
                if OLDS in m.linkname:
                    m.linkname = m.linkname.replace(OLDS, NEWS)
                    n += 1
                dst.addfile(m)
            elif m.isreg():
                data = src.extractfile(m).read()
                c = data.count(OLD)
                if c:
                    data = data.replace(OLD, NEW)
                    n += c
                dst.addfile(m, io.BytesIO(data))
            else:
                dst.addfile(m)
    enc.stdin.close()
    drain(dec)
    if enc.wait() != 0:
        raise SystemExit("zstd compress failed")
    os.replace(tmp, path)
    return n

def main(root):
    archives = sorted(os.path.join(d, f) for d, _, fs in os.walk(root) for f in fs if f.endswith(".tzst"))
    patched = []
    for a in archives:
        c = scan(a)
        if c:
            print("patching %s: %d occurrence(s)" % (a, c), flush=True)
            print("  rewrote %d" % rewrite(a), flush=True)
            patched.append(a)
    if not any(p.endswith("rootfs.tzst") for p in patched):
        raise SystemExit("rootfs.tzst was not patched")
    bad = [(a, scan(a)) for a in patched if scan(a)]
    if bad:
        raise SystemExit("old path still present: %s" % bad)
    print("OK: patched %d archive(s), no old path left" % len(patched))

main(sys.argv[1])
