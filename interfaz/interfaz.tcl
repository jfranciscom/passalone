#############################################################################
# Generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#  Oct 28, 2019 03:17:18 PM EDT  platform: Linux
set vTcl(timestamp) ""


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(active_menu_fg) #000000
}




proc vTclWindow.top42 {base} {
    global vTcl
    if {$base == ""} {
        set base .top42
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background $vTcl(actual_gui_bg) 
    wm focusmodel $top passive
    wm geometry $top 354x389+383+141
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1351 738
    wm minsize $top 1 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "Sistema de autenticacion"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    ttk::style configure PC.TNotebook -background $vTcl(actual_gui_bg)
    ttk::style configure PC.TNotebook.Tab -background $vTcl(actual_gui_bg)
    ttk::style configure PC.TNotebook.Tab -foreground $vTcl(actual_gui_fg)
    ttk::style configure PC.TNotebook.Tab -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style layout PC.TNotebook.Tab {
                    Notebook.tab -children {
                        Notebook.padding -side top -children {
                            Notebook.focus -side top -children {
                                Notebook.text -side right
                                Notebook.image -side left
                            }
                        }
                    }
               }
    vTcl::widgets::ttk::pnotebook::createCmd $top.pNo44 \
        -width 322 -height 326 -takefocus {} -style "PC.TNotebook" 
    vTcl:DefineAlias "$top.pNo44" "tabs" vTcl:WidgetProc "Toplevel1" 1
    $top.pNo44 configure -style "PC.TNotebook"
    bind $top.pNo44 <Button-1> {
        _button_press
    }
    bind $top.pNo44 <ButtonRelease-1> {
        _button_release
    }
    bind $top.pNo44 <Motion> {
        _mouse_over
    }
    frame $top.pNo44.t0 \
        -background $vTcl(actual_gui_bg) -highlightcolor black 
    vTcl:DefineAlias "$top.pNo44.t0" "tabs_t1" vTcl:WidgetProc "Toplevel1" 1
    $top.pNo44 add $top.pNo44.t0 \
        -padding 0 -sticky nsew -state normal -text Agendar -image image2 \
        -compound none -underline -1 
    set site_4_0  $top.pNo44.t0
    entry $site_4_0.ent45 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -insertbackground black 
    vTcl:DefineAlias "$site_4_0.ent45" "txnombre" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_0.lab46 \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -text Nombre 
    vTcl:DefineAlias "$site_4_0.lab46" "Label1" vTcl:WidgetProc "Toplevel1" 1
    entry $site_4_0.ent47 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -insertbackground black 
    vTcl:DefineAlias "$site_4_0.ent47" "txapellido" vTcl:WidgetProc "Toplevel1" 1
    entry $site_4_0.ent48 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -insertbackground black 
    vTcl:DefineAlias "$site_4_0.ent48" "txdoc" vTcl:WidgetProc "Toplevel1" 1
    entry $site_4_0.ent49 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -insertbackground black 
    vTcl:DefineAlias "$site_4_0.ent49" "txdatosadic" vTcl:WidgetProc "Toplevel1" 1
    entry $site_4_0.ent50 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -insertbackground black 
    vTcl:DefineAlias "$site_4_0.ent50" "txidsocio" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_0.lab51 \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -text Apellido 
    vTcl:DefineAlias "$site_4_0.lab51" "Label2" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_0.lab52 \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -text Documento 
    vTcl:DefineAlias "$site_4_0.lab52" "Label3" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_0.lab53 \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -text {Fecha nac.} 
    vTcl:DefineAlias "$site_4_0.lab53" "Label4" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_0.lab54 \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -text {Nro. de socio} 
    vTcl:DefineAlias "$site_4_0.lab54" "Label5" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_0.lab55 \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -text {Datos adic.} 
    vTcl:DefineAlias "$site_4_0.lab55" "Label6" vTcl:WidgetProc "Toplevel1" 1
    entry $site_4_0.ent56 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -insertbackground black 
    vTcl:DefineAlias "$site_4_0.ent56" "txrenovday" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_0.lab57 \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -text {Fecha renov.} 
    vTcl:DefineAlias "$site_4_0.lab57" "Label7" vTcl:WidgetProc "Toplevel1" 1
    entry $site_4_0.ent58 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -insertbackground black 
    vTcl:DefineAlias "$site_4_0.ent58" "txrenovmonth" vTcl:WidgetProc "Toplevel1" 1
    entry $site_4_0.ent59 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -insertbackground black 
    vTcl:DefineAlias "$site_4_0.ent59" "txrenovyear" vTcl:WidgetProc "Toplevel1" 1
    entry $site_4_0.ent60 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -insertbackground black 
    vTcl:DefineAlias "$site_4_0.ent60" "txnacday" vTcl:WidgetProc "Toplevel1" 1
    entry $site_4_0.ent61 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -insertbackground black 
    vTcl:DefineAlias "$site_4_0.ent61" "txnacmonth" vTcl:WidgetProc "Toplevel1" 1
    entry $site_4_0.ent62 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -insertbackground black 
    vTcl:DefineAlias "$site_4_0.ent62" "txnacyear" vTcl:WidgetProc "Toplevel1" 1
    button $site_4_0.but63 \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text Button 
    vTcl:DefineAlias "$site_4_0.but63" "Button1" vTcl:WidgetProc "Toplevel1" 1
    button $site_4_0.but64 \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text {Agendar afiliado} 
    vTcl:DefineAlias "$site_4_0.but64" "btagendar" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_0.lab78 \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -text Resultado: 
    vTcl:DefineAlias "$site_4_0.lab78" "Label16" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_0.lab79 \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -text Preparado. 
    vTcl:DefineAlias "$site_4_0.lab79" "lbagendarstatus" vTcl:WidgetProc "Toplevel1" 1
    place $site_4_0.ent45 \
        -in $site_4_0 -x 120 -y 20 -anchor nw -bordermode ignore 
    place $site_4_0.lab46 \
        -in $site_4_0 -x 10 -y 20 -anchor nw -bordermode ignore 
    place $site_4_0.ent47 \
        -in $site_4_0 -x 120 -y 50 -width 166 -relwidth 0 -height 23 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_0.ent48 \
        -in $site_4_0 -x 120 -y 80 -anchor nw -bordermode ignore 
    place $site_4_0.ent49 \
        -in $site_4_0 -x 120 -y 170 -anchor nw -bordermode ignore 
    place $site_4_0.ent50 \
        -in $site_4_0 -x 120 -y 140 -anchor nw -bordermode ignore 
    place $site_4_0.lab51 \
        -in $site_4_0 -x 10 -y 50 -anchor nw -bordermode ignore 
    place $site_4_0.lab52 \
        -in $site_4_0 -x 5 -y 80 -width 89 -relwidth 0 -height 21 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_0.lab53 \
        -in $site_4_0 -x 10 -y 110 -anchor nw -bordermode ignore 
    place $site_4_0.lab54 \
        -in $site_4_0 -x 10 -y 140 -anchor nw -bordermode ignore 
    place $site_4_0.lab55 \
        -in $site_4_0 -x 10 -y 170 -anchor nw -bordermode ignore 
    place $site_4_0.ent56 \
        -in $site_4_0 -x 120 -y 200 -width 36 -relwidth 0 -height 23 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_0.lab57 \
        -in $site_4_0 -x 10 -y 200 -anchor nw -bordermode ignore 
    place $site_4_0.ent58 \
        -in $site_4_0 -x 180 -y 200 -width 36 -relwidth 0 -height 23 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_0.ent59 \
        -in $site_4_0 -x 240 -y 200 -width 36 -relwidth 0 -height 23 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_0.ent60 \
        -in $site_4_0 -x 120 -y 110 -width 36 -relwidth 0 -height 23 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_0.ent61 \
        -in $site_4_0 -x 180 -y 110 -width 36 -relwidth 0 -height 23 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_0.ent62 \
        -in $site_4_0 -x 240 -y 110 -width 36 -relwidth 0 -height 23 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_0.but63 \
        -in $site_4_0 -x 190 -y 240 -width -59 -relwidth 0 -height 31 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_0.but64 \
        -in $site_4_0 -x 20 -y 240 -width 261 -relwidth 0 -height 21 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_0.lab78 \
        -in $site_4_0 -x 20 -y 270 -anchor nw -bordermode ignore 
    place $site_4_0.lab79 \
        -in $site_4_0 -x 100 -y 270 -anchor nw -bordermode ignore 
    frame $top.pNo44.t1 \
        -background $vTcl(actual_gui_bg) -highlightcolor black 
    vTcl:DefineAlias "$top.pNo44.t1" "tabs_t2" vTcl:WidgetProc "Toplevel1" 1
    $top.pNo44 add $top.pNo44.t1 \
        -padding 0 -sticky nsew -state normal -text Renovar -image image2 \
        -compound none -underline -1 
    set site_4_1  $top.pNo44.t1
    entry $site_4_1.ent66 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -insertbackground black 
    vTcl:DefineAlias "$site_4_1.ent66" "txrenovaciondias" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_1.lab67 \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -text {Ingrese la cantidad de dias a extender.} 
    vTcl:DefineAlias "$site_4_1.lab67" "Label8" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_1.lab68 \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -text dias. 
    vTcl:DefineAlias "$site_4_1.lab68" "Label9" vTcl:WidgetProc "Toplevel1" 1
    button $site_4_1.but70 \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text {Extender plazo} 
    vTcl:DefineAlias "$site_4_1.but70" "txrenovar" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_1.lab71 \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -text Resultado: 
    vTcl:DefineAlias "$site_4_1.lab71" "Label10" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_1.lab72 \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -text {En espera de operaciones.} 
    vTcl:DefineAlias "$site_4_1.lab72" "Label11" vTcl:WidgetProc "Toplevel1" 1
    place $site_4_1.ent66 \
        -in $site_4_1 -x 20 -y 50 -width 96 -relwidth 0 -height 23 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_1.lab67 \
        -in $site_4_1 -x 20 -y 20 -anchor nw -bordermode ignore 
    place $site_4_1.lab68 \
        -in $site_4_1 -x 120 -y 50 -anchor nw -bordermode ignore 
    place $site_4_1.but70 \
        -in $site_4_1 -x 20 -y 90 -width 261 -relwidth 0 -height 31 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_1.lab71 \
        -in $site_4_1 -x 20 -y 140 -anchor nw -bordermode ignore 
    place $site_4_1.lab72 \
        -in $site_4_1 -x 106 -y 141 -width 175 -height 21 -anchor nw \
        -bordermode ignore 
    frame $top.pNo44.t2 \
        -background $vTcl(actual_gui_bg) -highlightcolor black 
    vTcl:DefineAlias "$top.pNo44.t2" "tabs_t3" vTcl:WidgetProc "Toplevel1" 1
    $top.pNo44 add $top.pNo44.t2 \
        -padding 0 -sticky nsew -state normal -text {Consultar datos} \
        -image {} -compound none -underline -1 
    set site_4_2  $top.pNo44.t2
    label $site_4_2.lab73 \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -text Estado: 
    vTcl:DefineAlias "$site_4_2.lab73" "Label12" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_2.lab74 \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -text {Datos obtenidos:} 
    vTcl:DefineAlias "$site_4_2.lab74" "Label13" vTcl:WidgetProc "Toplevel1" 1
    button $site_4_2.but75 \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text {Consultar datos} 
    vTcl:DefineAlias "$site_4_2.but75" "btconsultar" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_2.lab76 \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -text {Apoye la tarjeta, la huella y continue.} 
    vTcl:DefineAlias "$site_4_2.lab76" "Label14" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_2.lab77 \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -text Preparado. 
    vTcl:DefineAlias "$site_4_2.lab77" "Label15" vTcl:WidgetProc "Toplevel1" 1
    text $site_4_2.tex82 \
        -background white -font TkTextFont -foreground black -height 134 \
        -highlightcolor black -insertbackground black \
        -selectbackground #c4c4c4 -selectforeground black -state disabled \
        -width 286 -wrap word 
    .top42.pNo44.t2.tex82 configure -font "TkTextFont"
    .top42.pNo44.t2.tex82 insert end text
    vTcl:DefineAlias "$site_4_2.tex82" "txdataconseguida" vTcl:WidgetProc "Toplevel1" 1
    place $site_4_2.lab73 \
        -in $site_4_2 -x 20 -y 100 -anchor nw -bordermode ignore 
    place $site_4_2.lab74 \
        -in $site_4_2 -x 20 -y 140 -anchor nw -bordermode ignore 
    place $site_4_2.but75 \
        -in $site_4_2 -x 20 -y 60 -width 261 -relwidth 0 -height 31 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_2.lab76 \
        -in $site_4_2 -x 20 -y 20 -width 279 -relwidth 0 -height 31 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_2.lab77 \
        -in $site_4_2 -x 80 -y 100 -anchor nw -bordermode ignore 
    place $site_4_2.tex82 \
        -in $site_4_2 -x 20 -y 160 -width 286 -relwidth 0 -height 134 \
        -relheight 0 -anchor nw -bordermode ignore 
    button $top.but80 \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text Salir 
    vTcl:DefineAlias "$top.but80" "btsalir" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.pNo44 \
        -in $top -x 20 -y 10 -width 322 -relwidth 0 -height 326 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but80 \
        -in $top -x 240 -y 340 -width 101 -relwidth 0 -height 31 -relheight 0 \
        -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top42 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

