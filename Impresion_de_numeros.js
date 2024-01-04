function run() {
        var presentacion = "Vamos a imprimir los números desde el 1000 hasta en 5000 de 1 en 1";
        console.log(presentacion);
        run2();
    }
    
    function run2() {
        var numbersde5en5 = Array.from({ length: (5000 - 1000) / 1 + 1 }, (_, index) => 1000 + index * 1);
        console.log(numbersde5en5);
    }
    
    if (require.main === module) {
        run();
    }
    