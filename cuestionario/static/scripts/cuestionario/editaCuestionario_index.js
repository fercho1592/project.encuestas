/**
 * @version   0.1
 * @author    Fernando Alvarez Flores <feral1592@gmail.com>
 *
 * History
 * v0.1 - La primera versión Fernando Alvarez Flores
 **/

$().ready(function()
{
	$.each($(".id_pregunta"),function(){
		var url = "/cuestionario/p"+$(this).text();
		$.ajax({
			url: url,
			async: false,
			success:function(data, textStatus, jqXHR,$anterior=1){
				$("#preguntas").append(data);
				//Carga las respuestas
			},
			error:ErrorFunction,
			beforeSend: Wait,
			complete: Continue,
		});
		$(this).remove();
	})

	inicializa();
});

//Se encarga de buscar el siguiente elemento a modificar
//@param {jQuery object} $elemento -> objeto actual
function buscaSiguente($elemento){
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

function inicializa(){
	$("input[name$='pregunta']").change(function(){
		var form = $(this).parents(".form");
		var data = form.children().serialize();
		var url = "/cuestionario/"+form.attr("id");

		$.ajax({
			type: "POST",
			url: url,
			data: data,
			success:function(data, textStatus, jqXHR,$anterior=form){
				$anterior.parents(".panel").before(data);
				$anterior.parents(".panel").remove();
				inicializa();
			},
			error:ErrorFunction,
		});
	});

	//Cuando se desea agregar una nueva pregunta
	$("#pN input[name$='pregunta']").change(function(){
		var form = $(this).parents(".form");
		var data = form.children().serialize();

		$.ajax({
			type: "POST",
			url: "/cuestionario/pN/",
			data: data,
			success:function(resultado,$anterior=1){
				$("#preguntas").append(resultado);
			},
			error:ErrorFunction,
		});

		$(this).val("");
	});
}