
/* initialize the datatable manually */

//function getCookie(cname) {
//    var name = cname + "=";
//    var ca = document.cookie.split(';');
//    for(var i=0; i<ca.length; i++) {
//        var c = ca[i];
//        while (c.charAt(0)==' ') c = c.substring(1);
//        if (c.indexOf(name) == 0) return c.substring(name.length,c.length);
//    }
//    return "";
//}; 
//
//var csrftoken = getCookie('csrftoken');

$.fn.editable.defaults.mode = 'popup';

datatableview.auto_initialize = false;

//function csrfSafeMethod(method) {
//    // these HTTP methods do not require CSRF protection
//    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
//}
//$.ajaxSetup({
//    beforeSend: function(xhr, settings) {
//        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
//            xhr.setRequestHeader("X-CSRFToken", csrftoken);
//        }
//    }
//});

$( function() {

	var xeditable_options = {
        error: function(data) {
            /* actions on validation error (or ajax error) */
    
        	var msg = '';

        	if(data.errors) { //validation error
                $.each(data.errors, function(k, v) { msg += k+": "+v+"<br>"; });  
            } else if(data.responseText) { //ajax error, get form_errors text
            	$.each(jQuery.parseJSON(data.responseText).form_errors, function(k, v) { msg += v+"<br>"; });	
            	$('.editable-error-block').html(msg); 
            }

        },

	};

    return datatableview.initialize( $('.datatable'), {

    	language: {
    		lengthMenu: "&nbsp;Show _MENU_ entries",
    	},

//    	dom: 'Blfrtip',
//    	buttons: [
//	        'pdf',
//	        'csv',
//	        'print',
//	        'selectAll',
//	        'selectNone',
//	        {
//	            extend: 'selected',
//	            text: 'Flag as audited',
//	            action: function ( e, dt, button, config ) {
//	            	console.log(dt.rows( { selected: true } ).data());
//	            	$.ajax({
//	            		url: '/uploads/',
//	            		type: 'POST',
//	            		data: dt.rows( { selected: true } ).data(),
////	            		data: {
////	            			'csrftoken': getCookie('csrftoken'),
////	            			'uploads': dt.rows( { selected: true } ).data(),
////	            			},
//	                	});
//	            }
//	        },
//        ],

        fnRowCallback: datatableview.make_xeditable(xeditable_options),

    });    

});

//table.columns().flatten().each( function ( colIdx ) {
//    // Create the select list and search operation
//    var select = $('<select />')
//        .appendTo(
//            table.column(colIdx).footer()
//        )
//        .on( 'change', function () {
//            table
//                .column( colIdx )
//                .search( $(this).val() )
//                .draw();
//        } );
// 
//    // Get the search data for the first column and add to the select list
//    table
//        .column( colIdx )
//        .cache( 'search' )
//        .sort()
//        .unique()
//        .each( function ( d ) {
//            select.append( $('<option value="'+d+'">'+d+'</option>') );
//        } );
//} );
//new $.fn.dataTable.Buttons( table, {
//    buttons: [
//		'copyHtml5',
//		'excelHtml5',
//		'csvHtml5',
//		'pdfHtml5'
//		]
//} );
// 
//table.buttons().container()
//    .appendTo( $('.col-sm-6:eq(0)', table.table().container() ) );
//
