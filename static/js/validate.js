$.fn.extend({
    'validate':function(re){
        if($(this).val()==""){
            if($(this).required()) return false;
            else return true;
        }
        return $(this).val().match((re||$(this).data('re')));
    },
    'add_validate':function(type,callback)
   {
    var re;
    if(typeof(type)=='undefined') type='email';
    else{
        var regexp={
            'name':/\D{2,20}/,
            'email':/([\w\d_\.]+)@(([\w\d]+\.)+\w{1,5})/,
            'mobile':/(\d{11})/,
            'twitter':/@[\w\d_]+/,
            'student_number' : /(0[0-8]|13|14|15)(08|09|10|11)([1-9]\d)(\d\d)/,
        }
        if(!(re=regexp[type]))
        {
            re=regexp['email'];
            type='email';
        }
    }
   $(this).data({'re':re})
    var vali=function(){
        var match=$(this).validate();
        if($(this).val().length==0){
            if($(this).data('required'))
                callback.call($(this), 'required',null,null);
            else
                callback.call($(this), 'empty',null,null);
        }
        else if(match) callback.call($(this),'valid',type,match);
        else  callback.call($(this),'invalid',type,$(this).val())
    }
    return $(this)
        .focus(vali)
        .bind('keyup',vali)
        .bind('blur',
                function(){
                    if((!$(this).data('required')) && $(this).val()=="") callback.call($(this),'normal')
                    else vali.call($(this));
                });
   },
    'required':function(bool){
        if(typeof(bool)!='undefined')
                return $(this).data({'required':bool});
        else return $(this).data('required');
    },
    'number_only':function(){
        $(this).bind('keydown',function(e)
                {
                    if(!((e.keyCode>=48 && e.keyCode<=58 )|| (e.keyCode>=35 && e.keyCode<=37)|| e.keyCode==39 ||e.keyCode==8 ||e.keyCode==9))return false;
                    return true;
                }).bind('afterpaste',function(){$(this).val($(this).val().replace(/\D/g,''))})
        .bind('change',function(){$(this).val($(this).val().replace(/\D/g,''))});
    }
})
