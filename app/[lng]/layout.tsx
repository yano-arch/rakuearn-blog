import type { Metadata } from "next";
import { languages } from "@/app/i18n/settings";
import { Geist, Geist_Mono, Noto_Sans_JP } from "next/font/google";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

const notoSansJp = Noto_Sans_JP({
  variable: "--font-noto-sans-jp",
  subsets: ["latin"],
  weight: ["400", "500", "700"],
});

const SITE_URL = "https://rakuearn-blog.vercel.app";
const SITE_NAME = "ミリオン記事速報";
const SITE_DESCRIPTION =
  "SNSやニュースで注目のトピックを毎日リサーチし、わかりやすい記事にまとめてお届けします。";

export const metadata: Metadata = {
  metadataBase: new URL(SITE_URL),
  title: {
    default: `${SITE_NAME} | 今話題のニュースを、わかりやすく`,
    template: `%s | ${SITE_NAME}`,
  },
  description: SITE_DESCRIPTION,
  openGraph: {
    siteName: SITE_NAME,
    title: `${SITE_NAME} | 今話題のニュースを、わかりやすく`,
    description: SITE_DESCRIPTION,
    url: SITE_URL,
    type: "website",
  },
  twitter: {
    card: "summary",
    title: `${SITE_NAME} | 今話題のニュースを、わかりやすく`,
    description: SITE_DESCRIPTION,
  },
  robots: {
    index: true,
    follow: true,
  },
  verification: {
    google: "BG2Q2lTcIvihYc377j9Bq-N9i3npiwnM1jVhqzTKAtY",
  },
};

export async function generateStaticParams() {
  return languages.map((lng) => ({ lng }));
}

// export async function generateMetadata() {
//   const { t } = await getT('common')
//   return {
//     title: t('howItWorks')
//   }
// }

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="ja">
      <body
        className={`${geistSans.variable} ${geistMono.variable} ${notoSansJp.variable} antialiased bg-white`}
      >
        {children}
      </body>
    </html>
  );
}
