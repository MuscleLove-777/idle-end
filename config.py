"""放置ゲーム引退ブログ - ブログ固有設定"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

BLOG_NAME = "放置ゲーム引退ブログ"
BLOG_DESCRIPTION = "放置ゲームから卒業したい人向けの実践ガイド。卒業手順・喪失感対処・乗り換え先紹介・家庭内信用回復まで、ニッチだが需要のある「やめ方」特化メディア。"
BLOG_URL = "https://musclelove-777.github.io/idle-end/"
BLOG_LANGUAGE = "ja"
GITHUB_REPO = "MuscleLove-777/idle-end"

TARGET_CATEGORIES = [
    "ガチ卒業10ステップ",
    "サブ垢処分ガイド",
    "喪失感メンタル対策",
    "乗り換え先ゲーム提案",
    "嫁/恋人バレ後の信用回復",
    "課金履歴の整理",
    "ゲーム時間の代替活動",
]

THEME = {
    "primary": "#264653",
    "accent": "#e76f51",
    "gradient_start": "#264653",
    "gradient_end": "#e76f51",
}

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.5-flash"
GEMINI_FALLBACK_MODEL = "gemini-2.5-flash-lite"

OUTPUT_DIR = BASE_DIR / "output"
ARTICLES_DIR = OUTPUT_DIR / "articles"
SITE_DIR = OUTPUT_DIR / "site"
TOPICS_DIR = OUTPUT_DIR / "topics"

MAX_ARTICLE_LENGTH = 4000
SEO_KEYWORD_DENSITY = 0.02
