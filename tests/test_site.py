"""Run with: python -m unittest discover -s tests -v"""
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]
PAGES = ('index.html', 'terms.html', 'privacy.html', 'support.html', 'data-deletion.html')

class Document(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.tags = []
        self.links = []
        self.ids = []
        self.text = text
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append((tag, attrs))
        if tag == 'a' and 'href' in attrs:
            self.links.append(attrs['href'])
        if 'id' in attrs:
            self.ids.append(attrs['id'])

class SiteTests(unittest.TestCase):
    def test_policy_pages_exist_and_are_accessible_documents(self):
        for name in PAGES:
            with self.subTest(page=name):
                path = ROOT / name
                self.assertTrue(path.is_file(), f'Missing required page: {name}')
                doc = Document(path.read_text(encoding='utf-8'))
                self.assertEqual(sum(tag == 'h1' for tag, _ in doc.tags), 1)
                self.assertTrue(any(tag == 'html' and a.get('lang') == 'en' for tag, a in doc.tags))
                for required in ('title', 'main', 'nav', 'footer'):
                    self.assertTrue(any(tag == required for tag, _ in doc.tags), f'{name}: missing {required}')
                self.assertTrue(any(tag == 'meta' and a.get('name') == 'viewport' for tag, a in doc.tags))
                self.assertEqual(len(doc.ids), len(set(doc.ids)), 'Duplicate IDs')
                self.assertFalse(any(tag in ('script', 'iframe', 'form') for tag, _ in doc.tags), 'Policy site must not collect data or load executable third-party content')
                for marker in ('TODO', 'YOUR_APP', 'your-email', 'example.com', 'INSERT HERE'):
                    self.assertNotIn(marker, doc.text)
                for link in doc.links:
                    parts = urlsplit(link)
                    self.assertNotEqual(parts.scheme, 'javascript')
                    if parts.scheme or parts.netloc:
                        continue
                    target = (path.parent / unquote(parts.path)).resolve() if parts.path else path
                    self.assertTrue(target.is_relative_to(ROOT))
                    self.assertTrue(target.is_file(), f'Broken link: {name} -> {link}')
                    if parts.fragment:
                        dest = Document(target.read_text(encoding='utf-8'))
                        self.assertIn(parts.fragment, dest.ids)
                for policy in ('terms.html', 'privacy.html', 'support.html', 'data-deletion.html'):
                    self.assertIn(policy, doc.links)

if __name__ == '__main__':
    unittest.main()
