import { NavBar } from "@/components/Navbar";

export function Main() {
    return (
        <main className="h-screen bg-home text-white">
        <NavBar />
        <div className="w-max mt-[10%] mx-auto text-center">
          <h1 className="text-6xl w-[54rem]">Nunca mais esqueça um aniversário importante</h1>
          <h2 className="mt-11 text-[#ccc]">Celebre cada momento especial - deixe-nos lembrar os aniversários por você</h2>
        </div>
      </main>
    )
}