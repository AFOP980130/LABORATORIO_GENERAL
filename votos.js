let votos = []

function votar(candidatos){
    votos.push(candidatos)
}

function contarVotos(){
    let conteo = {};
    for(let i = 0; i < votos.length; i++){
        let voto = votos[i];
        if (conteo [voto] === undefined) {
            conteo[voto]=1;
        }   else {
            conteo[voto]++;
        }
    }
    return conteo;
}

votar("Pedro");

votar("Pedre");

votar("Pedra");

console.log(contarVotos());