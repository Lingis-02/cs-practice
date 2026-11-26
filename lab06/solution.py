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

def human_size(n_bytes):
    if n_bytes < 1024:
        return f"{n_bytes} Б"

    size = float(n_bytes)
    for unit in ["Кб", "Мб", "Гб", "Тб"]:
        size /= 1024.0
        if size < 1024.0 or unit == "Тб":
            return f"{size:.1f} {unit}"

    return f"{size:.1f} Тб"

