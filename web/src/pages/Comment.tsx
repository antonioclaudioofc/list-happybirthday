import { CardComment } from "@/components/CardComment";

export function Comment() {
    return (
        <section className="bg-[#ccc] text-center pt-16 pb-20">
            <h2 className="text-4xl">Depoimentos</h2>
            <h3 className="text-xl mt-6 mb-9">Veja o que nossos usuários têm a dizer sobre o nosso serviço de lembrete de aniversário</h3>
            <div className="flex flex-wrap justify-center gap-4">
                <CardComment />
                <CardComment />
                <CardComment />
            </div>
        </section>
    )
}