interface PropsServices {
    title: string,
    describe: string
}

export default function CardService(props: PropsServices) {
    return (
        <div className="w-96">
            <div className="h-96 bg-slate-300 rounded-lg"></div>
            <h4 className="text-2xl mt-2 mb-2">{props.title}</h4>
            <p className="text-justify">{props.describe}</p>
        </div>
    )
}