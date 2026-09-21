import { NextResponse } from 'next/server'
import { languages, headerName } from './app/i18n/settings'

export const config = {
  matcher: [
    '/((?!api|_next/static|_next/image|assets|favicon.ico|sw.js|site.webmanifest).*)',
    '/((?!_next/static|_next/image|favicon.ico|.*\\.(?:svg|png|jpg|jpeg|gif|webp)$).*)',
  ]
}

const defaultLng = 'ja'

const seoRoutes = new Set(['/sitemap.xml', '/robots.txt'])

export function middleware(req) {
  const pathname = req.nextUrl.pathname

  if (pathname.indexOf('icon') > -1 || pathname.indexOf('chrome') > -1) {
    return NextResponse.next()
  }

  // /sitemap.xml and /robots.txt must stay at the site root (that's where
  // Google and other crawlers look for them) — never locale-prefixed.
  if (seoRoutes.has(pathname)) {
    return NextResponse.next()
  }

  const lngInPath = languages.find((loc) => pathname.startsWith(`/${loc}`))

  if (
    !lngInPath &&
    !pathname.startsWith('/_next') &&
    !pathname.startsWith('/api') &&
    !pathname.endsWith('.html')
  ) {
    // Avoid appending "/" for the root path — "/" + "/" produces "/ja/",
    // which Next.js then 308-redirects again to "/ja" (trailingSlash: false
    // is the default), turning every visit to "/" into a two-hop redirect
    // chain ("/" -> "/ja/" -> "/ja"). Google Search Console flagged this
    // ("ページにリダイレクトがあります") on the /ja page. Redirecting straight
    // to "/ja" collapses it to a single hop.
    const suffix = pathname === '/' ? '' : pathname
    return NextResponse.redirect(
      new URL(`/${defaultLng}${suffix}${req.nextUrl.search}`, req.url)
    )
  }

  const response = NextResponse.next()
  response.headers.set(headerName, lngInPath || defaultLng)
  return response
}
