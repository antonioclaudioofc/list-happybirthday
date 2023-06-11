import { CardService } from "@/components/CardService";
import { NavBar } from "@/components/Navbar";

export default function Home() {
  return (
    <>
      <main className="h-screen bg-home text-white">
        <NavBar />
        <div className="w-max mt-[10%] mx-auto text-center">
          <h1 className="text-6xl w-[54rem]">Nunca mais esqueça um aniversário importante</h1>
          <h2 className="mt-11 text-[#ccc]">Celebre cada momento especial - deixe-nos lembrar os aniversários por você</h2>
        </div>
      </main>
      <section className="text-center mt-16">
        <h2 className="text-4xl">Recursos</h2>
        <h3 className="text-xl mt-6 mb-9">Explore as vantagens exclusivas do nosso serviço de lembrete de aniversário</h3>

        <div className="w-3/4 mx-auto flex flex-wrap gap-9 justify-center">
          <CardService
            title="Notificação por e-mail"
            describe="Nunca esqueça um aniversário importante! Receba lembretes por e-mail e surpreenda seus entes queridos."
          />
          <CardService
            title="Notificação por e-mail"
            describe="Nunca esqueça um aniversário importante! Receba lembretes por e-mail e surpreenda seus entes queridos."
          />
          <CardService
            title="Notificação por e-mail"
            describe="Nunca esqueça um aniversário importante! Receba lembretes por e-mail e surpreenda seus entes queridos."
          />
          <CardService
            title="Notificação por e-mail"
            describe="Nunca esqueça um aniversário importante! Receba lembretes por e-mail e surpreenda seus entes queridos."
          />
        </div>
      </section>
    </>
  )
}
