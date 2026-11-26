from pathlib import PurePosixPath


def count_by_extension(paths):
    counts = {}
    for path in paths:
        filename = PurePosixPath(path).name
        if "." in filename:
            ext = filename.rsplit(".", 1)[1].lower()
        else:
            ext = ""
        counts[ext] = counts.get(ext, 0) + 1
    return counts

def deepest_path(paths):
    if not paths:
        return ""
    return min(paths, key=lambda p: (-p.count("/"), p))

