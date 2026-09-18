import { NextResponse } from 'next/server'
import { languages, headerName } from './app/i18n/settings'

export const config = {
  matcher: [
    '/((?!api|_next/static|_next/image|assets|favicon.ico|sw.js|site.webmanifest).*)',
    '/((?!_next/static|_next/image|favicon.ico|.*\\.(?:svg|png|jpg|jpeg|gif|webp)$).*)',
  ]
}

const defaultLng = 'ja'

export function middleware(req) {
  const pathname = req.nextUrl.pathname

  if (pathname.indexOf('icon') > -1 || pathname.indexOf('chrome') > -1) {
    return NextResponse.next()
  }

  const lngInPath = languages.find((loc) => pathname.startsWith(`/${loc}`))

  if (
    !lngInPath &&
    !pathname.startsWith('/_next') &&
    !pathname.startsWith('/api') &&
    !pathname.endsWith('.html')
  ) {
    return NextResponse.redirect(
      new URL(`/${defaultLng}${pathname}${req.nextUrl.search}`, req.url)
    )
  }

  const response = NextResponse.next()
  response.headers.set(headerName, lngInPath || defaultLng)
  return response
}
