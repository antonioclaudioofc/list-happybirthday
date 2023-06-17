import CardService from "@/components/CardService";

export default function Services() {
    return (
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
    )
}