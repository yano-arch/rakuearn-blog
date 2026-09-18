import { ReactNode } from "react";

interface LayoutProps {
  children: ReactNode;
}

export const Layout: React.FC<LayoutProps> = ({ children }) => {
  return (
    <main className="mx-auto max-sm:overflow-x-hidden my-0 bg-white flex flex-col items-center" aria-label="Main content">
      {children}
    </main>
  );
};