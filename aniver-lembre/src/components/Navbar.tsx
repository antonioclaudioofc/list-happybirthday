import Image from 'next/image';
import imgLogo from '../../public/logo.svg';


export function NavBar() {
    return (
        <nav className="flex justify-around items-center pt-9">
            <Image
                src={imgLogo}
                alt="Tente"
            />
            <ul className="flex gap-12">
                <li>Início</li>
                <li>Recursos</li>
                <li>Como Funciona</li>
                <li>Depoimentos</li>
                <li>Contato</li>
            </ul>
            <button className="py-3 px-11 text-[#dadada] bg-[#1C74BC] rounded-3xl">Login</button>
        </nav>
    )
}