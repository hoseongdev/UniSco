import type { Metadata } from "next";
import { Geist_Mono } from "next/font/google";
// 2026-08-25 리디자인 — Geist(라틴 전용)는 이 앱의 한글 위주 UI에선 실제로 한 글자도
// 못 그려서(한글 글리프가 없어 전부 시스템 폴백 Arial로 렌더링되고 있었음, globals.css의
// body font-family가 애초에 이 변수를 아예 안 쓰고 있던 것도 같은 맥락) 그동안 사실상
// 죽은 설정이었음 — 한글까지 커버하는 Pretendard Variable로 교체. 토스·뱅크샐러드 등
// 한국 핀테크 앱들이 표준처럼 쓰는 서체라 "토스 느낌"에 필요한 타이포 밀도·자신감 있는
// 굵기 대비를 그대로 가져올 수 있음. 숫자(금액 등)는 Geist Mono의 tabular 숫자를 그대로
// 살려서 씀(font-mono 유틸리티로 선택 적용, ScholarshipResults 등 참고).
import "pretendard/dist/web/variable/pretendardvariable-dynamic-subset.css";
import "./globals.css";

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "UniSco",
  description: "대전 지역 대학생을 위한 맞춤형 장학금 매칭",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html
      lang="ko"
      className={`${geistMono.variable} antialiased`}
    >
      <body className="flex flex-col">{children}</body>
    </html>
  );
}
