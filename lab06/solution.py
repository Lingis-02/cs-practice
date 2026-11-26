from pathlib import PurePosixPath


def count_by_extension(paths):
    counts = {}
    for path in paths:
        ext = PurePosixPath(path).suffix.lstrip(".").lower()
        counts[ext] = counts.get(ext, 0) + 1
    return counts

def deepest_path(paths):
    if not paths:
        return ""
    return min(paths, key=lambda p: (-p.count("/"), p))

def human_size(n_bytes):
    if n_bytes < 1024:
        return f"{n_bytes} Б"

    size = float(n_bytes)
    for unit in ["КБ", "МБ", "ГБ", "ТБ"]:
        size /= 1024.0
        if size < 1024.0 or unit == "ТБ":
            return f"{size:.1f} {unit}"

    return f"{size:.1f} ТБ"

