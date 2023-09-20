(function () {
    const btnEliminacion=document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn=>{
        btn.addEventListener('click', (e)=>{
            const confirmacion=confirm('¿Desea proseguir con la eliminación del curso?');
            if(!confirmacion){
                e.preventDefault();
            }
        });
    });
})();