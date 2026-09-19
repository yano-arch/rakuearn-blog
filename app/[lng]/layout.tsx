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

export const metadata: Metadata = {
  title: "ミリオン記事速報 | 今話題のニュースを、わかりやすく",
  description: "SNSやニュースで注目のトピックを毎日リサーチし、わかりやすい記事にまとめてお届けします。",
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
