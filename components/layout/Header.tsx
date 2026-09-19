"use client";
import React from "react";
import Link from "next/link";
import Image from "next/image";
import { useParams } from "next/navigation";
import { useT } from "@/app/i18n/client";
import Logo from "@/assets/images/logo.svg";

const Header: React.FC = () => {
  const { t } = useT("common");
  const lng = useParams().lng as string;

  return (
    <header
      className="flex items-center justify-between py-6 w-full"
      aria-label="Header"
    >
      <Link href={`/${lng}`} className="flex items-center gap-3">
        <Image src={Logo} alt={t("siteName")} className="w-[140px]" priority />
      </Link>
      <nav className="flex items-center gap-6" aria-label="Main navigation">
        <Link href={`/${lng}`} className="text-sm font-bold text-black">
          {t("home")}
        </Link>
        <Link href={`/${lng}/ranking`} className="text-sm font-bold text-black">
          {t("ranking")}
        </Link>
      </nav>
    </header>
  );
};

export default Header;
