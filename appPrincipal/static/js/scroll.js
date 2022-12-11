let ubicacionPrincipal = this.window.pageYOffset
let $nav = document.querySelector('#nav')

window.addEventListener('scroll', function() {
    let ubicacionActual = this.window.pageYOffset

    console.log(ubicacionPrincipal);

    if(ubicacionPrincipal >= ubicacionActual){
        $nav.style.top = '950px'
    } else{
        $nav.style.top = '-350px'
    }

    ubicacionPrincipal = ubicacionActual
})

