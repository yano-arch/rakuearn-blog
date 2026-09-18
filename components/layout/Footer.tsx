"use client";
import React from "react";
import { useParams } from "next/navigation";
import { useT } from "@/app/i18n/client";

interface FooterProps {
  className?: string;
}

const Footer: React.FC<FooterProps> = ({ className }) => {
  const lng = useParams().lng as string;
  const { t } = useT("common");
  const year = new Date().getFullYear();

  return (
    <footer
      className={`py-10 w-full flex flex-col items-center gap-2 border-t border-neutral-100 text-sm text-neutral-500 ${
        className ?? ""
      }`}
      aria-label="Footer"
    >
      <p className="font-bold text-black">{t("siteName")}</p>
      <p>
        &copy; {year} {t("siteName")}
      </p>
    </footer>
  );
};

export default Footer;
