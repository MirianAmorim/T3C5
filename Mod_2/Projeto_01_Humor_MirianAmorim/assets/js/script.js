const elementoNome = document.getElementById('nome');
const elementoSituacao = document.querySelector('#situacao');
const elementoImg = document.querySelector('#imagem');
let elementoBtn = document.querySelector('#alterar');

elementoBtn.addEventListener('click', () =>{
    
    if(elementoBtn.value == 'primeiro'){
        elementoImg.src = './assets/img/santinho.png' 
        elementoNome.innerText = 'Eu juro!!' 
        elementoSituacao.innerText = 'Não fiz nada!' 
        elementoBtn.value = 'segundo' 
    } else if(elementoBtn.value == 'segundo') { 
        elementoImg.src = './assets/img/bem_loco.png' 
        elementoNome.innerText = 'Te Enganei!!! kkkk'
        elementoSituacao.innerText = 'Lelo lelo kkk'
        elementoBtn.value = 'terceiro'
    } else { 
        elementoImg.src = './assets/img/santo.png'
        elementoNome.innerText = '      Não fui eu!!      '
        elementoSituacao.innerText = 'Acredita em mim! Olha a minha carinha de santo!'
        elementoBtn.value = 'primeiro'
    }
})
