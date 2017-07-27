/**
 * @fileoverview Menú aprMenu, desplegable con efecto expansión suavizado
 *
 * @version                               2.2
 *
 * @author                 César Krall <cesarkrall@aprenderaprogramar.com>
 * @copyright           aprenderaprogramar.com
 *
 * History
 * v0.1 – Se mejoró el efecto de expansión de los submenús dándole efecto aceleración
 *
 * La primera versión Fernando Alvarez Flores
        */

$().ready(function()
{
	//Cuando se pulse enter o un boton, hacer que se mande esa informacion al server y 
	//poner la respuesta en donde estaba ese bloke, ademas crea otro objeto abajo de 
	//este para crear otra pregunta
	$("input").keyup(function(e){
	    if(e.keyCode == 13)
	    {
	    	var sig = buscaSiguente($(this));
	    	if(sig!==null)
	    		sig.focus();
	    	else
	    		$(this).blur();
	    }
	});

	$("input[name$='pregunta']").blur(function(){
		var valor = $(this).val();
		if("pN"==$(this).parents(".form").attr("id"))
		{
			$.ajax({
		        type: "POST",
		        url: "",
		        contentType: "application/json; charset=utf-8",
		        data: {pregunta : valor,},
		        dataType: "json",
		        success: function (resultado) {
		            $("#dataBaseStatus").text(resultado);
		        },
		        error: ErrorFunction
		        beforeSend: Wait,
		        complete: Continue,
		    });
			//Crea nueva pregunta y carga la respuesta del servidor
			//Cambia el focus a la primera pregunta
			console.log(1);
		}
		else
		{
			//Modifica el valor de la pregunta
			console.log(0);
		}
	})
});


/**
 * El comentario comienza con una barra y dos asteriscos.
* Cada nueva línea lleva un asterisco al comienzo.
 * @param {string} nombre indica que una función recibe un parámetro de tipo string y que
          * el nombre del parámetro es nombre.
 * @descriptor Cada descriptor que añadamos irá en una línea independiente.
        */        
function buscaSiguente($elemento)
{
	var sig =null;
	var father = $elemento.parents(".form");
    var brothers = father.children(".cuesElemento");
    var index = brothers.index($elemento);
    if(brothers.length>index+1)
    	sig =father.children(".cuesElemento")[index+1].focus();
    else
    {
    	index$= $(".form").index(father);
    	if($(".form").length>index+1)
    	{
    		var aunt = $($(".form")[index]);
    		if(aunt.children(".cuesElemento:first-child").length!=0)
    			sig = aunt.children(".cuesElemento:first-child");
    	}
    }

    return sig;
}