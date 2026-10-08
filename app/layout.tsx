import './globals.css';
import type { Metadata } from 'next';
export const metadata: Metadata={title:'trimzee — Book your next look',description:'Real-time salon booking for Pune.'};
export default function RootLayout({children}:{children:React.ReactNode}){return <html lang="en"><body>{children}</body></html>}