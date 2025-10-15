# Chrome Release / Listing Prep

# Release Prep

## Release Prep

- [ ]  in `inflow/apps/careerops-extension` `pnpm run prepare-release #.#.#`

# Listing Prep

## Tooling

### Job Link Examples

https://stripe.com/jobs/search

https://zapier.com/jobs#job-openings

[https://openai.com/careers/search/](https://openai.com/careers/search/)

### Tools

- window resize chrome extension
- Screenshot: CleanShot
- Screen Studio

## Screenshots

- [ ]  **Localized screenshots** (5x 1280x800 or 640x400)
    - [ ]  rename `ssLocal.extCtxtJobStripe.1280x800.png`
- [ ]  **Localized promo video**
- [ ]  **Global screenshots** (5x 1280x800 or 640x400)
    - [ ]  rename `ssGlobal.extCtxtJobStripe.1280x800.png`
- [ ]  **Global promo video**
- [ ]  **Small promo tile** (1320x840→440x280 Canvas)
    - [ ]  rename `promoTile.extCtxtJobStripe.1320x840.png`
- [ ]  **Marquee promo tile** (1400x560 Canvas)
    - [ ]  rename `marquee.extCtxtJobStripe.1400x560.png`
- [ ]  Resize
    - [ ]  run resize script `pnpm run resize-screenshots` in `Sites/inflow/`

## Copy

- [ ]  grab from `inflow/assets/careerops/chromestore-listing/releases/v0.5.2/copy/v0.5.2-listing.md`
- [ ]  load into [Chomestore Copy Table](Chromestore%20Copy%202336509554a780588fedfe6c80c8b5b7.md)

# LandingPage Prep

## Tools

- [window resize extension](https://chromewebstore.google.com/detail/window-resizer/kkelicaakdanhinjdeammmilcgefonfh)
- [Screen Studio](https://screen.studio/)

## Demo Capture

- [ ]  **Hero ext demo**
    - [ ]  put in `inflow/apps/careerops-web/public/videos`
    - [ ]  name `extCropJobCapture`
- [ ]  **Capture Context Demo** (Stripe - [https://stripe.com/jobs/listing/product-manager-link/6070194](https://stripe.com/jobs/listing/product-manager-link/6070194))
    - [ ]  put in `inflow/apps/careerops-web/public/videos`
    - [ ]  rename `extCtxtJobCapture`
- [ ]  **Track Context Demo**  (Zuk - [https://www.linkedin.com/in/mark-zuckerberg-618bba58/](https://www.linkedin.com/in/mark-zuckerberg-618bba58/))
    - [ ]  put in `inflow/apps/careerops-web/public/videos`
    - [ ]  rename `extCtxtPplCapture`
- [ ]  **Export Context Demo** (Zapier - [https://jobs.ashbyhq.com/zapier/9c09aca7-3abb-49ae-acd7-d12d35188a1d](https://jobs.ashbyhq.com/zapier/9c09aca7-3abb-49ae-acd7-d12d35188a1d))
    - [ ]  put in `inflow/apps/careerops-web/public/videos`
    - [ ]  rename `extCtxtCSVExport`