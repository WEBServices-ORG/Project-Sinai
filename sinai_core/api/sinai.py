# Sinai Core API


class Sinai:
    """Core Sinai AI class."""

    def __init__(self):
        self.initialized = True

    def ask(self, query: str, k: int = 5) -> list:
        """Process a Torah AI query and return results."""
        # Simple implementation for demo
        query_lower = query.lower()
        has_hebrew = any("\u0590" <= c <= "\u05ff" for c in query)
        if "genesis 1:1" in query_lower or "בראשית" in query:
            if has_hebrew:
                answer = "בראשית א:א (עברית: בְּרֵאשִׁית בָּרָא אֱלֹהִים אֵת הַשָּׁמַיִם וְאֵת הָאָרֶץ).\nרש״י מסביר: 'בראשית' מתייחס לתורה, תחילת חכמתו של אלוהים."
            else:
                translit_part = (
                    " (Transliteration: Bereshit bara Elohim et hashamayim ve'et ha'aretz)"
                    if "translate" in query_lower
                    else ""
                )
                answer = f"Genesis 1:1{translit_part}. Rashi explains: 'In the beginning' refers to the Torah, the beginning of God's wisdom."
        elif "rashi" in query_lower or "רש״י" in query:
            answer = (
                "Rashi (Rabbi Shlomo Yitzchaki) was a medieval French rabbi and author of a comprehensive commentary on the Talmud and the Hebrew Bible."
                if not has_hebrew
                else "רש״י (הרב שלמה יצחקי) היה רב צרפתי בימי הביניים ומחבר פירוש מקיף על התלמוד והמקרא העברי."
            )
        else:
            answer = (
                f"Response to '{query}': This is a demo response. Sinai AI is under development."
                if not has_hebrew
                else f"תגובה ל'{query}': זו תגובה דמו. בינה מלאכותית סיני בפיתוח."
            )
        if has_hebrew:
            answer = "\u200f" + answer
        source = "רש״י" if has_hebrew else "Rashi"
        return [{"answer": answer, "source": source}]

    def process_query(self, query: str) -> str:
        """Process a Torah AI query."""
        return f"Processed: {query}"

    def get_status(self) -> dict:
        """Get system status."""
        return {"status": "active", "version": "6.4", "name": "Project Sinai"}
