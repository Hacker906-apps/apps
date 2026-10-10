# Hacker Apps — Static Download Directory

A GitHub Pages-compatible, app-only catalogue. It uses HTML/CSS/vanilla JavaScript and JSON data; no database, API or backend is required.

## Files
- `index.html`: home page, search, category/platform filters and theme/language controls.
- `data/apps.json`: app catalogue. This is the main source of truth.
- `data/categories.json`: category names and Arabic labels.
- `build.py`: generates one indexable static HTML page per published app and refreshes `sitemap.xml`.
- `assets/css/style.css`: responsive visual system.
- `assets/js/app.js`: catalogue loading/search/filtering.
- `assets/js/theme.js`: theme preference and system default.
- `assets/js/ads.js`: supplied ad network script placements.

## Add, edit or remove an app
1. Put its image in `assets/images/` (SVG, WebP, PNG or JPG are fine).
2. Add one object to `data/apps.json`, with a unique lowercase `id`, accurate description, category, platforms and verified official/download URLs.
3. Set `published` to `true`. To hide a listing, set it to `false` or remove it from the JSON file.
4. Run `python3 build.py` to regenerate individual SEO pages and `sitemap.xml`.
5. Commit and push the complete folder to the `apps` directory of the `hacker906-apps.github.io` repository.

Do not use a download URL unless you have checked that it belongs to the official project or a trusted distributor. Blank version and update fields are intentionally shown as unspecified, not invented.

## Ads
The scripts supplied by the site owner are placed in labeled containers in the home page and app detail pages. Ads are kept separate from download buttons. The direct-link URL appears only as a clearly labeled, user-initiated sponsored link; it is not triggered automatically or placed beside a download button.

The ad scripts are third-party code and can affect page performance, privacy and user experience. Check the ad network's policies, GitHub Pages rules and applicable privacy requirements before going live.

## SEO and deployment
- This is a project site, so its canonical base is `https://hacker906-apps.github.io/apps/`.
- Run `python3 build.py` after editing app JSON. JavaScript-only cards are not treated as individual SEO pages; the generated `/apps/<id>/index.html` pages provide unique HTML titles, descriptions, canonical URLs and SoftwareApplication structured data.
- After publishing, check `https://hacker906-apps.github.io/apps/sitemap.xml` and submit it in Google Search Console. Indexing and ranking are not guaranteed.
- Test on mobile, test all official/download links, validate JSON, and run PageSpeed Insights. Ad scripts may reduce performance scores.
- GitHub Pages serves static files only; it cannot run `build.py` on the server. Run the build locally before committing.

## Local preview
Run from this folder: `python3 -m http.server 8000` and open `http://localhost:8000/`. The site should be tested over HTTP, not by opening `index.html` as a `file://` URL, because the catalogue is loaded with `fetch()`.
