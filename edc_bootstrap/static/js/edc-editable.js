$.fn.editable.defaults.mode = 'popup';
        datatableview.auto_initialize = false;
        $(function(){
            var xeditable_options = {
            		error: function(data) {
            	        /* actions on validation error (or ajax error) */
            	        var msg = '';
            	        if(data.errors) {              //validation error
            	        	$.each(data.errors, function(k, v) { msg += k+": "+v+"<br>"; });  
            	        } else if(data.responseText) {   //ajax error
            	        	$.each(jQuery.parseJSON(data.responseText).form_errors, function(k, v) { msg += v+"<br>"; });	
            	        	$('.editable-error-block').html(msg); 
            	        }
            	    },
            };
            datatableview.initialize($('.datatable'), {
                fnRowCallback: datatableview.make_xeditable(xeditable_options),
            });
        });