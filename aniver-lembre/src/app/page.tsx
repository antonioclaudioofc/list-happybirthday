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
      <section className="text-center mt-16 mb-16">
        <h2 className="text-4xl">Recursos</h2>
        <h3 className="text-xl mt-6 mb-9">Explore as vantagens exclusivas do nosso serviço de lembrete de aniversário</h3>

        <div className="w-3/4 mx-auto flex flex-wrap gap-9 justify-center mt-24">
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
      <section className="bg-[#26ABE2] text-white flex flex-col justify-center items-center">
        <h2 className="pt-16 pb-6 text-4xl">Como Funciona</h2>
        <ul className="flex flex-col gap-2">
          <li>
            Cadastre-se em segundos: Não perca tempo, comece a lembrar aniversários agora mesmo!
          </li>
          <li>
            Adicione eventos com facilidade: Nunca mais esqueça um aniversário importante, apenas alguns cliques e está feito!
          </li>
          <li>
            Gerencie sua lista de eventos: Mantenha tudo organizado e atualizado, sem confusão!
          </li>
          <li>
            Notificações personalizadas: Receba lembretes no seu estilo, exatamente quando você precisa.
          </li>
          <li>
            Celebre com emoção: Surpreenda seus entes queridos com desejos de aniversário especiais e faça cada momento memorável.
          </li>
        </ul>
        <button className="px-8 py-3 mt-10 mb-20 bg-transparent border border-black text-black rounded-3xl">
          Contato
        </button>
      </section>
      <section className="bg-[#ccc]">
        <h2 className="text-4xl">Depoimentos</h2>
        <h3 className="text-xl mt-6 mb-9">Veja o que nossos usuários têm a dizer sobre o nosso serviço de lembrete de aniversário</h3>
      </section>
    </>
  )
}
