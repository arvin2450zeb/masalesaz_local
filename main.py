import random
import sys
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles


def resource_path(relative_path: str) -> Path:
    """Find a project resource in development or in a PyInstaller bundle."""
    bundle_dir = getattr(sys, "_MEIPASS", None)
    base_dir = Path(bundle_dir) if bundle_dir else Path(__file__).resolve().parent
    return base_dir / relative_path


WEB_DIR = resource_path("web")
app = FastAPI(title="مسئله‌ساز ریاضی")
app.mount("/static", StaticFiles(directory=str(WEB_DIR)), name="static")

ANIMALS = {
    "اسب": ("اسب", 4),
    "خروس": ("خروس", 2),
    "گاو": ("گاو", 4),
    "هشت‌پا": ("هشت‌پا", 8),
    "گوسفند": ("گوسفند", 4),
    "گربه": ("گربه", 4),
    "عنکبوت": ("عنکبوت", 8),
    "لاک‌پشت": ("لاک‌پشت", 4),
    "اردک": ("اردک", 2),
    "سگ": ("سگ", 4),
    "خرگوش": ("خرگوش", 4),
    "بوقلمون": ("بوقلمون", 2),
    "شیر": ("شیر", 4),
    "فیل": ("فیل", 4),
    "میمون": ("میمون", 2),
    "قورباغه": ("قورباغه", 4),
    "مورچه": ("مورچه", 6),
    "زنبور": ("زنبور", 6),
    "عقرب": ("عقرب", 8),
    "خرچنگ": ("خرچنگ", 10),
    "پنگوئن": ("پنگوئن", 2),
    "کانگورو": ("کانگورو", 2),
    "تمساح": ("تمساح", 4),
    "دایناسور": ("دایناسور", 4),
}

PROBLEM_TYPES = [
    ("اسب", "خروس"),
    ("گاو", "هشت‌پا"),
    ("خروس", "گوسفند"),
    ("گربه", "عنکبوت"),
    ("لاک‌پشت", "اردک"),
    ("گوسفند", "عنکبوت"),
    ("سگ", "خروس"),
    ("اردک", "خرگوش"),
    ("گربه", "خروس"),
    ("گاو", "بوقلمون"),
    ("شیر", "خروس"),
    ("فیل", "اردک"),
    ("میمون", "گوسفند"),
    ("مورچه", "عنکبوت"),
    ("زنبور", "عقرب"),
    ("پنگوئن", "خرگوش"),
    ("کانگورو", "خروس"),
    ("تمساح", "اردک"),
    ("دایناسور", "گوسفند"),
    ("خرچنگ", "هشت‌پا"),
    ("شیر", "فیل"),
    ("میمون", "لاک‌پشت"),
]


@app.get("/", include_in_schema=False)
def home():
    return FileResponse(WEB_DIR / "index.html")


@app.get("/api/status")
def status():
    return {
        "message": "Problem Generator API is running!",
        "animals_count": len(ANIMALS),
        "problem_types_count": len(PROBLEM_TYPES),
    }


@app.post("/problems/generate")
def generate():
    animal1_key, animal2_key = random.choice(PROBLEM_TYPES)
    animal1_name, animal1_legs = ANIMALS[animal1_key]
    animal2_name, animal2_legs = ANIMALS[animal2_key]

    count1 = random.randint(1, 20)
    count2 = random.randint(1, 20)
    total_heads = count1 + count2
    total_legs = count1 * animal1_legs + count2 * animal2_legs

    problem = (
        f"تعدادی {animal1_name} و {animal2_name} داریم. "
        f"مجموع سرهای آن‌ها {total_heads} و "
        f"تعداد پاهای آن‌ها {total_legs} است. "
        f"تعداد هرکدام را مشخص کنید. "
        f"[{animal1_name} = {animal1_legs}]، [{animal2_name} = {animal2_legs}]"
    )

    return {
        "problem": problem,
        "answer": {animal1_key: count1, animal2_key: count2},
    }
