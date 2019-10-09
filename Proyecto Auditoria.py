# -*- coding: utf-8 -*-
import statistics
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd


PoliticasSeguridad = []

OrganizationSeguridad = []
OrganizacionInterna = [] 
PartesExternas = []

AdministracionActivos = []
ResponsibilidadActivos = []
ClasificacionInformacion = []		

SeguridadRH = []	
PrevioEmpleo = []
DuranteEmpleo = []
TerminacionEmpleo = []

SeguridadFA = []	
AreasSegura = [] 
EquipamientoSeguridad = []	

ComunicacionesOperaciones = []
ProcedimientosOperativas = []
ManejoTercerizados	= []
PlaneamientoSistemas = []	
ProteccionMovil = []	
CopiasRespaldo = []	
AdministracionRed = []
ManejoMedios = []
IntercambioInformacion = []			
ServiciosElectronico = []			
Monitoreo = []		

AccessControl = []
RequerimientosControlAcceso = []	
AdministracionUsuarios  = []	
ResponsabilidadesUsuarios = []	
ControlAccesoRed = []	
ControlesAccesoSistO = []	
ControlAccesoInformacion = []		
ComputacionMovilTeletrabajo = []
		
DeAdManSistemas = []
RequerimientosSeguridadInformacion = []	
ProcesamientoAplicaciones = []
ControlesCriptograficos	= []
SeguridadSistemas = []
SeguridadServiciosSoporte = []	
GestionVulnerabilidadesTecnicas = []
		
GestionIncidentes = []	
ReportandoVulnerabilidades = []	
GestionProcesoMejoras = []	


GestionContinuidad = []
AspectosContinuidadNegocio =[]

Cumplimiento = []			
CumplimientoLegales	= []		
CumplimientoRegulacionesTecnicas = []	
ConsideracionesSistemas = []

	
valores25 = int
valores75 = int
valores100 = int
suma = int

promedio = int

def plot_bar_x():
        # this is for plotting purpose
          index = np.arange(len(etiquetas))
          plt.bar(index, datos)
          plt.xlabel('Secciones', fontsize=5)
          plt.ylabel('Promedios', fontsize=5)
          plt.xticks(index,etiquetas, fontsize=5, rotation=90)
          plt.title('Promedios de Secciones')
          plt.show()

def menu():
    print ("Selecciona una opción")
    print ("\t1 - Chequeo por cumplimiento")
    print ("\t2 - Cumplimiento por control")
    print ("\t3 - Cumplimiento por Dominio")
    print ("\t4 - Representación Gráfica")
    print ("\t5 - Etiqueta")
    print ("\t9 - salir")
    

while True:
	# Mostramos el menu
    menu()
 
	# solicituamos una opción al usuario
    opcionMenu = input("inserta un numero valor >> ")
   
    if opcionMenu=="1":
        
        print ("*****Seccion: Política de Seguridad*********")
        print ("*****Documento de la Política de Seguridad de Información*********")
        a=int(input("Existe una Política de Seguridad de la Información, que es aprobada por la dirección, publicada y comunicada según proceda, a todos los empleados?"))
        PoliticasSeguridad.append(a)
        a=int(input("Establecen las políticas un compromiso de las Gerencias con relación al método de la organización para la gestión de la seguridad de la información?"))
        PoliticasSeguridad.append(a)
        
        print ("***** Revisión de la Política de Seguridad*********")
        a=int(input("Las políticas de seguridad son revisadas a intervalos regulares, o cuando hay cambios significativos para asegurar la adecuación y efectividad?"))
        PoliticasSeguridad.append(a)
        a=int(input("Las políticas de seguridad son revisadas a intervalos regulares, o cuando hay cambios significativos para asegurar la adecuación y efectividad?"))
        PoliticasSeguridad.append(a)
        a=int(input("Existen procedimientos de revisión de las políticas de seguridad y estos incluyen requerimientos para el manejo de su revisión?"))
        PoliticasSeguridad.append(a)
        a=int(input("Los resultados del revisión de la gestión son tenidos en cuenta?"))
        PoliticasSeguridad.append(a)
        a=int(input("Se obtiene la aprobación de la alta gerencia con relació a las políticas revisadas?"))
        PoliticasSeguridad.append(a)
        
        print("******Seccion: Organization de la Seguridad de Información	******")				

        print ("***** Gestión de Compromiso con la Seguridad de Información*********")
        a=int(input("Si la gerencia demuestra soporte activo a las medidas de seguridad dentro de la organización. Esto puede ser realizado por direcciones claras, compromiso demostrado, asignaciones explícitas y conocimiento de las responsabilidades de la seguridad de información."))
        OrganizationSeguridad.append(a)
        OrganizacionInterna.append(a)
        
        print ("***** Coordinación de la Seguridad de Información*********")
        a=int(input("Si las actividades de seguridad de información son coordinadas por representantes de distintas partes de la organización, con sus roles pertinentes y responsabilidades."))
        OrganizationSeguridad.append(a)
        OrganizacionInterna.append(a)
        
        print ("***** Asignación de Responsabilidades de Seguridad de Información*********")
        a=int(input("Están establecidas las responsabilidades de protección de activos individuales y llevar a cabo procesos de seguridad específicos que estén claramente identificados y definidos?"))
        OrganizationSeguridad.append(a)
        OrganizacionInterna.append(a)
        
        print ("***** Proceso de autorizacion de instalaciones de Procesamiento de Información*********")
        a=int(input("Si el proceso de gestión de autorización está definido e implementado para cada nuevo equipo de procesamiento de información dentro de la organización. "))
        OrganizationSeguridad.append(a)
        OrganizacionInterna.append(a)
        
        print ("*****  Acuerdos de Confidencialidad*********")
        a=int(input("Si el proceso de gestión de autorización está definido e implementado para cada nuevo equipo de procesamiento de información dentro de la organización. "))
        OrganizationSeguridad.append(a)
        OrganizacionInterna.append(a)
        
        a=int(input("¿Tiene esta dirección la exigencia de proteger la información confidencial utilizando términos legales exigibles?"))
        OrganizationSeguridad.append(a)
        OrganizacionInterna.append(a)
        
        print ("***** Contacto con las Autoridades*********")
        a=int(input("Existe algún procedimiento que describa cuando y quienes deben contactar a las autoridades competentes, departamento de bomberos, etc y cómo deben reportarse los incidentes? "))
        OrganizationSeguridad.append(a)
        OrganizacionInterna.append(a)
        
        print ("***** Contacto con Grupos de Intereses Especiales*********")
        a=int(input("Existen los contactos apropiados con grupos especiales de interés, foros de seguridad o asociaciones profesionales relacionadas con la seguridad?"))
        OrganizationSeguridad.append(a)
        OrganizacionInterna.append(a)
        print ("*****  Revisión Independiente sobre la Seguridad de Información*********")
        a=int(input("Tiene la organización un enfoque sobre la gestión de la seguridad de información, su implementación, revisión independiente a intervalos regulares o cuando ocurran cambios significativos?"))
        OrganizationSeguridad.append(a)
        OrganizacionInterna.append(a)
        
        print ("***** Administración de Activos***** ")
        
        
        a=int(input("Los riesgos inherentes a equipos o sistemas de información de terceros son identificados y luego implementadas medidas de control apropiadas antes de permitir el acceso?"))
        OrganizationSeguridad.append(a)
        PartesExternas.append(a)
        
        print ("***** Abordar la seguridad al tratar con los clientes*********")
        a=int(input("Son identificados todos los requerimientos de seguridad sean cumplidos antes de conceder acceso a los clientes a los activos de la organización?"))
        OrganizationSeguridad.append(a)
        PartesExternas.append(a)
        
        print ("***** Abordar la seguridad en acuerdos con terceros*********")
        a=int(input("Los acuerdos con terceros incluyen accesos, procesamiento, comunicaciones, manejo de la información o equipos que involucren almacenamiento de información que cumplan con todos los requerimientos de seguridad?"))
        OrganizationSeguridad.append(a) 
        PartesExternas.append(a)
        
        
        print ("***** Seccion : Identificación de los riesgos relacionados con partes externas*********")
        
        print ("***** Inventario de Activos*********")
        a=int(input("Son los activos debi damente identificados e inventariados o se mantiene un registro de los activos importantes?"))
        AdministracionActivos.append(a)  
        ResponsibilidadActivos.append(a)
        
        print ("***** Propiedad de Activos *********")
        a=int(input("Son los activos debidamente identificados e inventariados o se mantiene un registro de los activos importantes?"))
        AdministracionActivos.append(a)  
        ResponsibilidadActivos.append(a)
        print ("***** Uso aceptable de Activos *********")
        a=int(input("Son identificadas, documentadas e implementadas todas las regulaciones existentes con respecto al uso aceptable de información y activos asociados con el procesamiento de información?"))
        AdministracionActivos.append(a)  
        ResponsibilidadActivos.append(a)
        
        
        print ("***** Directrices de Clasificación *********")
        a=int(input("La información es clasificada en terminos de su valor, requerimientos legales, sensibilidad y criticidad para la organización?"))
        AdministracionActivos.append(a)  
        ClasificacionInformacion.append(a)
        
        print ("***** Etiquetado y manejo de información*********")
        a=int(input("Son definidos conjuntos de procedimientos para etiquetado y manejo de la información en concordancia con el esquema de clasificación atoptado por la organización? "))
        AdministracionActivos.append(a)  
        ClasificacionInformacion.append(a)
        
        print ("*****Sección: Seguridad de Recursos Humanos	 *********")
       
        print ("***** Roles y Responsabilidades *********")
        a=int(input("Están claramente definidos y documentados de acuerdo a las políticas de seguridad de información de la organización los roles y responsabilidades de los empleados, contratistas y terceros?"))
        SeguridadRH.append(a) 
        PrevioEmpleo.append(a)
        
        a=int(input("Son los roles y responsabilidades definidos previamente, comunicados claramente a los candidatos a empleo durante el proceso de pre empleo?"))
        SeguridadRH.append(a)
        PrevioEmpleo.append(a)
        
        
        print ("***** Proyección *********")
        a=int(input("Los controles de verificación de antecedentes para todos los candidatos a empleo, contratistas y terceros, son llevados a cabo de acuerdo a las regulaciones relevantes?"))
        SeguridadRH.append(a)
        PrevioEmpleo.append(a)
        
        a=int(input("Incluye la verificación referencias sobre el carácter, confirmación de titulos académicos, cualidades profesionales y chequeos independientes de identidad?"))
        SeguridadRH.append(a) 
        PrevioEmpleo.append(a)
        
        print ("***** Términos y condiciones de empleo *********")
        a=int(input("Son firmados con los empleados, contratistas y terceros, contratos de confidencialidad y acuerdos de no divulgación como parte inicial de los términos y condiciones de contratos de trabajo?"))
        SeguridadRH.append(a)
        PrevioEmpleo.append(a)
        
        a=int(input("Estos acuerdos y contratos cubren las responsabilidades de seguridad de información de la organización, los empleados, contratistas y terceros?"))
        SeguridadRH.append(a)   
        PrevioEmpleo.append(a)
        
        
        print ("***** Administración de Responsabilidades*********")
        a=int(input("La gestión requiere a los empleados, contratistas y terceros a que apliquen la seguridad en concordancia con las Políticas y Procedimientos establecidos en la Organización?"))
        SeguridadRH.append(a)
        DuranteEmpleo.append(a)
        
        print ("*****Sensibilización, educación y formación sobre la Seguridad de la Información*********")
        a=int(input("Sensibilización, educación y formación sobre la Seguridad de la Información"))
        SeguridadRH.append(a) 
        DuranteEmpleo.append(a)
        
        
        print ("*****Proceso Disciplinario*********")
        a=int(input("Existe un proceso disciplinario para aquellos empleados que incumplen las políticas de seguridad?"))
        SeguridadRH.append(a)     
        DuranteEmpleo.append(a)
        
        print ("*****Responsabilidades de Terminación*********")
        a=int(input("Las responsabilidades de procedimiento de terminación o cambio de empleo están claramente definidas y asignadas? "))
        SeguridadRH.append(a)   
        TerminacionEmpleo.append(a)          

        print ("*****Retorno de activos*********")
        a=int(input("Existe un procedimiento a seguir con respecto a asegurar que los empleados, contratistas y terceros devuelvan los activos de la organización que estén en su poder al terminar el contrato de empleo?"))
        SeguridadRH.append(a) 
        TerminacionEmpleo.append(a)
        
        print ("*****Remoción de Derechos de Acceso Lógico*********")
        a=int(input("Son removidos los derechos de acceso de todos los empleados, contratistas y terceros a los sistemas de información al termino de empleo o adecuación en caso de que cambien de función?"))
        SeguridadRH.append(a)
        TerminacionEmpleo.append(a)

        print ("*****Seguridad Física y Ambiental*********")         
       
        print ("*****Perímetro de Seguridad Física*********")
        a=int(input("Existen mecanismos de control de acceso implementados con respecto al acceso a los sitios de procesamiento de información? Algunos ejemplos son controles biométricos, tarjetas de acceso, separación por muros, control de visitantes, etc."))
        SeguridadFA.append(a)
        AreasSegura.append(a)
         
        print ("*****Controles Físicos de Entrada*********")
        a=int(input("Existen controles de acceso de tal modo a que solo las personas autorizadas puedan ingresar a las distintas areas de la organización?"))
        SeguridadFA.append(a)
        AreasSegura.append(a)
        
        print ("*****Aseguramiento de Oficinas, Salas de Servidores e Instalaciones*********")
        a=int(input("Las salas de servidores u otros equipos de procesamiento (routers, switches, etc.), están apropiadamente resguardadas bajo llave o en cabinas con llave?"))
        SeguridadFA.append(a)
        AreasSegura.append(a)
        
        print ("*****Protección contra Amenazas Exteriores y Ambientales/Climáticas*********")
        a=int(input("Se tienen implementadas protecciones o resguardos contra fuego, inundaciones, temblores, explosiones, manifestaciones y otras formas de desastres naturales o provocadas por el hombre?"))
        SeguridadFA.append(a)
        AreasSegura.append(a)
        
        a=int(input("Existe alguna amenaza potencial en los locales vecinos del lugar donde se encuentran las instalaciones?"))
        SeguridadFA.append(a)
        AreasSegura.append(a)
        
    
        print ("*****Trabajando en Areas Seguras*********")
        a=int(input("Se tienen procedimientos designados e implementados sobre como trabajar en las areas seguras?"))
        SeguridadFA.append(a)
        AreasSegura.append(a)
        
            
        print ("*****Zonas de Acceso Público, Entrega y  Descarga*********")
        a=int(input("Con respecto a las zonas de acceso público, entrega, descarga donde personas no autorizadas pueden acceder, las zonas de procesamiento de información y equipos delicados son aislados y asegurados para prevenir el acceso no autorizado?"))
        SeguridadFA.append(a)
        AreasSegura.append(a)
        
        print ("*****Equipamiento y Protección del Sitio*********")
        a=int(input("Los equipos son protegidos para reducir los riesgos de daños ambientales y oportunidades de acceso no autorizado?"))
        SeguridadFA.append(a)
        EquipamientoSeguridad.append(a)
        
        
        print ("*****Utilidades Soportadas*********")
        a=int(input("Los equipos son protegidos contra fallas eléctricas y otras fallas que pudieran tener (redundancia)?"))
        SeguridadFA.append(a)
        EquipamientoSeguridad.append(a)
        a=int(input("Que mecanismos de protección eléctrica son utilizados? Alimentación multiple, UPS, generador de backup, etc?"))
        SeguridadFA.append(a)   
        EquipamientoSeguridad.append(a)             
        
        print ("*****Cableado de Seguridad*********")
        a=int(input("Los cables de suministro eléctrico y comunicaciones son debidamente protegidos contra intercepción y/o daños?"))
        SeguridadFA.append(a)
        EquipamientoSeguridad.append(a)
        a=int(input("Existen controles adicionales de seguridad con respecto al transporte de información crítica? Por ej. Encriptado en las comunicaciones."))
        SeguridadFA.append(a) 
        EquipamientoSeguridad.append(a)
         
        print ("****Mantenimiento de Equipos*********")        
        
        a=int(input("Se realiza mantenimiento periódico de los equipos de modo a asegurar la continua disponibilidad e integridad?"))
        SeguridadFA.append(a)
        EquipamientoSeguridad.append(a)
        a=int(input("En la realización de mantenimientos, son respetados los intervalos y recomendaciones de los fabricantes?"))
        SeguridadFA.append(a)
        EquipamientoSeguridad.append(a)
        a=int(input("Los mantenimientos son realizados unicamente por personal capacitado y autorizado?"))
        SeguridadFA.append(a)
        EquipamientoSeguridad.append(a)
        a=int(input("Los logs de alertas de los equipos, son revisados periodicamente para detectar y corregir posibles fallas en los mismos? (principalmente fallas en discos)"))
        SeguridadFA.append(a)       
        EquipamientoSeguridad.append(a)
        a=int(input("Se aplican los controles adecuados cuando se envían los equipos fuera de la organización?"))
        SeguridadFA.append(a)
        EquipamientoSeguridad.append(a)
        a=int(input("Todos los equipos están cubiertos por pólizas de seguro y los requerimientos de la Compañía de Seguros están apropiadamente realizados?"))
        SeguridadFA.append(a) 
        EquipamientoSeguridad.append(a)
        
        print ("****Aseguramiento de Equipos fuera de las Oficinas*********")     
        a=int(input("Existen mecanismos de control y mitigación de riesgos implementados con relación a equipos utilizados fuera de la organización? (encripción de discos de las notebooks, seguro, etc.)"))
        SeguridadFA.append(a)
        EquipamientoSeguridad.append(a)
        a=int(input("En caso de utilización de equipos fuera de la organización, estos cuentan con la autorización respectiva de las gerencias?"))
        SeguridadFA.append(a) 
        EquipamientoSeguridad.append(a)

        print ("****Disposiciones de Seguridad de Reutilización de Equipos *********")                
        a=int(input("Cuando se disponga la reutilización de equipos o cuando sean dados de baja, son verificados los medios de almacenamiento con respecto a datos y software licenciado y luego destruidos totalmente antes de su entrega?"))
        SeguridadFA.append(a)    
        EquipamientoSeguridad.append(a)
        
        print ("****Autorizaciones de Sacar Equipos*********")     
        a=int(input("Existen controles implementados con respecto a que ningún equipo, información y software sea sacado de la organización sin la autorización respectiva?"))
        SeguridadFA.append(a)
        EquipamientoSeguridad.append(a)
        
        print ("****Gestión de Comunicaciones y Operaciones		*********")
        
        print ("****Documentación de Procedimientos Operativos*********")     
        a=int(input("Los procedimientos operativos son documentados, actualizados y están disponibles para todos los usuarios que puedan necesitarlos?"))
        ComunicacionesOperaciones.append(a)
        ProcedimientosOperativas.append(a)
        a=int(input("Dichos procedimientos son tratados como documentos formales y cualquier cambio en los mismos necesita la autorización pertinente?"))
        ComunicacionesOperaciones.append(a)
        ProcedimientosOperativas.append(a)

        print ("****Manejo de Cambios*********")     
        a=int(input("Son controlados todos los cambios en los sistemas y equipos de procesamiento de información?"))
        ComunicacionesOperaciones.append(a)
        ProcedimientosOperativas.append(a)
        
        print ("****Segregación de Tareas*********")     
        a=int(input("Son separadas las tareas y responsabilidades de modo a reducir las oportunidades de modificación o mal uso de los sistemas de información?"))
        ComunicacionesOperaciones.append(a)  
        ProcedimientosOperativas.append(a)
                
        print ("****Separación de desarrollo, test e instalaciones operativas*********")     
        a=int(input("Los equipos de desarrollo y pruebas están separados de los equipos operacionales? Por ejemplo desarrollo de software debe estar en un equipo separado del de producción. Cuando sea necesario, incluso deben estar en segmentos de red distintos unos del otro."))
        ComunicacionesOperaciones.append(a) 
        ProcedimientosOperativas.append(a)
        
        print ("****Entrega de Servicios*********")     
        a=int(input("Existen medidas que son tomadas para asegurar que los controles de seguridad, niveles de servicio y entrega sean incluidos y verificados en los contratos de servicios con terceros, así como su revisión periódica de cumplimiento? "))
        ComunicacionesOperaciones.append(a) 
        ManejoTercerizados.append(a)

        print ("****Monitoreo y revisión de servicios tercerizados*********")     
        a=int(input("Son los servicios, reportes y registros proveídos por teceros regularmente monitoreados y revisados?"))
        ComunicacionesOperaciones.append(a) 
        ManejoTercerizados.append(a)
        
        print ("****Manejo de Cambios de servicios tercerizados*********")     
        a=int(input("Se gestionan los cambios en la provisión de servicios, incluyendo mantenimiento y la mejora en las políticas de seguridad de información existentes, procedimientos y controles?"))
        ComunicacionesOperaciones.append(a)   
        ManejoTercerizados.append(a)
        a=int(input("Se tienen en cuenta sistemas de negocio críticos, procesos involucrados y re-evaluación de riesgos?"))
        ComunicacionesOperaciones.append(a)    
        ManejoTercerizados.append(a)

        print ("****Gestión de la Capacidad*********")     
        a=int(input("La capacidad de procesamiento de los sistemas son monitoreados en base a la demanda y proyectados en base a requerimientos futuros, de modo a asegurar que la capacidad de proceso y almacenamiento estén disponibles? ‎Ejemplo: Monitoreo de espacio en disco, Memoria RAM, CPU en los servidores críticos."))
        ComunicacionesOperaciones.append(a)    
        PlaneamientoSistemas.append(a)
        
        print ("****Aceptación de Sistemas*********")     
        a=int(input("Son establecidos criterios de aceptación para nuevos sistemas de información, actualizaciones y nuevas versiones? Son realizadas pruebas antes de la aceptación de los mismos?"))
        ComunicacionesOperaciones.append(a)   
        PlaneamientoSistemas.append(a)
        
        
        print ("****Controles contra código malicioso********")     
        a=int(input("Existen controles para detección, prevención y recuperado contra código malicioso y son desarrollados e implementados procedimientos apropiados de advertencia a los usuarios?"))
        ComunicacionesOperaciones.append(a)   
        ProteccionMovil.append(a)
        print ("****Controles contra código movil********")     
        a=int(input("En caso de necesitarse código móvil, este solo debe utilizarse una vez que haya sido autorizado. ‎Las configuraciones del código móvil autorizado deben realizarse y operarse de acuerdo a las Políticas de Seguridad.‎ La ejecución del código móvil no autorizado, debe prevenirse. ‎‎(Código Móvil es código de software que se transfiere de una computadora a otra y que se ejecuta automáticamente. Realiza una función específica con muy poca o casi ninguna intervención del usuario.  El código móvil está asociado a un gran número de servicios de middleware)"))
        ComunicacionesOperaciones.append(a)  
        ProteccionMovil.append(a)
        
        print ("****Respaldo de la Información*********")     
        a=int(input("Se realizan copias de respaldo de la información y software y son testeados regularmente en conconrdancia con las políticas de backup?"))
        ComunicacionesOperaciones.append(a)   
        CopiasRespaldo.append(a)
        a=int(input("Toda la información y el software esencial puede ser recuperado en caso de ocurrencia de un desastre o fallo de medios?"))
        ComunicacionesOperaciones.append(a) 
        CopiasRespaldo.append(a)
        
        print ("****Controles de Red*********")     
        a=int(input("La red es adecuadamente administrada y controlada para protegerse de tretas y en orden a mantener la seguridad de los sistemas y aplicaciones en uso a traves de la red, incluyendo la información en transito?"))
        ComunicacionesOperaciones.append(a) 
        AdministracionRed.append(a)
        a=int(input("Existen controles implementados para asegurar el transito de la información en la red y evitar que esta sea leída o accesada de forma no autorizada? "))
        ComunicacionesOperaciones.append(a)   
        AdministracionRed.append(a)
        
        print ("****Seguridad en los Servicios de Red*********")                
        a=int(input("Las características de seguridad, niveles de servicio y requerimientos de administración de todos los servicios de red son identificados e incluidos en cualquier acuerdo de servicio de red?"))
        ComunicacionesOperaciones.append(a) 
        AdministracionRed.append(a)
        a=int(input("La capacidad del proveedor de servicios de red de proporcionar los servicios de forma segura, es determinada y regularmente monitoreada y se tienen derechos de auditoría acordada para medir niveles de servicio?"))
        ComunicacionesOperaciones.append(a) 
        AdministracionRed.append(a)
        
        
        print ("****Manejo de medios removibles*********")                
        a=int(input("Existen procedimientos para el manejo de medios removibles como cintas, diskettes, tarjetas de memoria, lectores de CD, pendrives, etc.?"))
        ComunicacionesOperaciones.append(a)  
        ManejoMedios.append(a)
        a=int(input("Los procedimientos y niveles de autorización están claramente definidos y documentados?"))
        ComunicacionesOperaciones.append(a)   
        ManejoMedios.append(a)
        
        print ("****Disposición de los medios*********")     
        a=int(input("En caso de que los medios ya no sean requeridos, estos son eliminados de forma segura bajo procedimientos formalmente establecidos?"))
        ComunicacionesOperaciones.append(a) 
        ManejoMedios.append(a)
        
        
        print ("****Procedimientos de manejo de la información*********")   
        a=int(input("Existen procedimientos para el manejo del almacenamiento de la información?"))
        ComunicacionesOperaciones.append(a)  
        ManejoMedios.append(a)
        
        a=int(input("Aborda este procedimiento temas como: protección de la información contra acceso no autorizado o mal uso?"))
        ComunicacionesOperaciones.append(a)
        ManejoMedios.append(a)
        
        print ("****Seguridad en la Documentación de los Sistemas*********")   
        a=int(input("La documentación de los sistemas está protegida contra acceso no autorizado?"))
        ComunicacionesOperaciones.append(a) 
        ManejoMedios.append(a)
        
        print ("****Políticas y Procedimientos de intercambio de información*********")   
        a=int(input("Existe una política formal, procedimientos y/o controles aplicados para asegurar la protección a la información?"))
        ComunicacionesOperaciones.append(a)
        IntercambioInformacion.append(a)
        a=int(input("Estos procedimientos y controles cubren el uso de equipos de comunicación electrónica en el intercambio de información?"))
        ComunicacionesOperaciones.append(a)
        IntercambioInformacion.append(a)
        
        print ("****Acuerdos de Intercambio*********")   
        a=int(input("Existen acuerdos de intercambio de información y software entre la organización y partes externas?"))
        ComunicacionesOperaciones.append(a)
        IntercambioInformacion.append(a)
        a=int(input("El contenido de los acuerdos con respecto a la seguridad refleja la sensibilidad y criticidad de la información de negocio envuelta en el proceso?"))
        ComunicacionesOperaciones.append(a)
        IntercambioInformacion.append(a)
        
        print ("****Medios físicos en transito*********")   
        a=int(input("Los medios físicos que contengan información es protegida contra acceso no autorizado, mal uso o corrupción de datos durante el transporte entre las organizaciones?"))
        ComunicacionesOperaciones.append(a)
        IntercambioInformacion.append(a)
        
        print ("****Mensajería Electrónica*********") 
        a=int(input("La información que se envía por mensajería electrónica es bien protegida?‎‎(Mensajería Electronica incluye pero no es restringida solamente a email, intercambio electrónico de datos, mensajería instantanea, etc."))
        ComunicacionesOperaciones.append(a)
        IntercambioInformacion.append(a)
        
        print ("****Sistema de información empresarial*********")   
        a=int(input("Las políticas y procedimientos son desarrolladas y tendientes a fortalecer la protección de información asociada con la interconexión de sistemas de negocio?"))
        ComunicacionesOperaciones.append(a)
        IntercambioInformacion.append(a)
        
        
        print ("****Comercio Electrónico*********")   
        a=int(input("La información envuelta en el comercio electrónico cruza a través de redes publicas y está protegida contra actividades fraudulenteas, posibles disputas contractuales o cualquier acceso no autorizado que permita lectura o manipulación de esos datos?"))
        ComunicacionesOperaciones.append(a)
        ServiciosElectronico.append(a)

        a=int(input("En los controles de seguridad son tenidos en cuenta la aplicación de controles criptográficos?"))
        ComunicacionesOperaciones.append(a)
        ServiciosElectronico.append(a)
        a=int(input("El comercio electrónico entre los socios comerciales incluyen un acuerdo, que compromete a ambas partes a la negociación de los términos convenidos, incluidos los detalles de las cuestiones de seguridad?"))
        ComunicacionesOperaciones.append(a)
        ServiciosElectronico.append(a)
        
        print ("****Transacciones On-line*********")
        a=int(input("La información envuelta en transacciones en línea está protegida contra transmisiones incompletas, mal ruteo, alteración de mensajería, divulgación no autorizada, duplicación no autorizada o replicación?"))
        ComunicacionesOperaciones.append(a)
        ServiciosElectronico.append(a)
        
        
        print ("****Información disponible públicamente*********")
        a=int(input("La integridad de la información disponible publicamente está protegida contra modificación no autorizada?"))
        ComunicacionesOperaciones.append(a) 
        ServiciosElectronico.append(a)

        print ("****Registros de Auditoría*********")
        a=int(input("Los registros de auditoría que guardan la actividad de los usuarios, excepciones, eventos de seguridad de información que ocurren, se guardan por un periodo razonable de tiempo de tal modo a poder realizar investigaciones futuras y monitoreo de acceso?"))
        ComunicacionesOperaciones.append(a)   
        Monitoreo.append(a)
        a=int(input("Se tienen en consideración medidas de protección a la privacidad en el mantenimiento de registros de auditoría?"))
        ComunicacionesOperaciones.append(a)   
        Monitoreo.append(a)

        print ("****Uso de Sistemas de Monitoreo*********")
        a=int(input("Son desarrollados procedimientos de monitoreo de equipos de procesamiento de datos?"))
        ComunicacionesOperaciones.append(a)  
        Monitoreo.append(a)
        a=int(input("El resultado de la actividad de monitoreo es revisada regularmente de forma periódica?"))
        ComunicacionesOperaciones.append(a)   
        Monitoreo.append(a)
        a=int(input("Los niveles de monitoreo requeridos por los equipos de procesamiento de información son determinados por un análisis de riesgos?"))
        ComunicacionesOperaciones.append(a)   
        Monitoreo.append(a)        
        

        print ("****Protección de los Logs*********")
        a=int(input("Los equipos que contienen los registros y logs de auditoría son bien protegidos contra posibles manipulaciones y acceso no autorizado?"))
        ComunicacionesOperaciones.append(a) 
        Monitoreo.append(a)
        
        print ("****Log de actividades de Administradores y Operadores*********")
        a=int(input("Las actividades de los Administradores y Operadores de sistemas son registradas en los logs?"))
        ComunicacionesOperaciones.append(a) 
        Monitoreo.append(a)
        
        a=int(input("Son revisados regularmente los logs?"))
        ComunicacionesOperaciones.append(a) 
        Monitoreo.append(a)
        
        print ("****Registro de Fallas*********")
        a=int(input("Las fallas son registradas en logs, y luego analizadas y acciones apropiadas realizadas en consecuencia?"))
        ComunicacionesOperaciones.append(a) 
        Monitoreo.append(a)

        a=int(input("Los niveles de registros en logs requeridos para cada sistema individual son determinados en base a análisis de riesgos y la degradación de performance es tenida en cuenta?‎"))
        ComunicacionesOperaciones.append(a) 
        Monitoreo.append(a)
        
        print ("****Sincronización de relojes*********")
        a=int(input("Los relojes de todos los sistemas de información están sincronizados en base a una misma fuente de tiempo exacta acordada?‎(La correcta sincronización de los relojes es importante para asegurar la cronología de eventos en los logs)‎"))
        ComunicacionesOperaciones.append(a) 
        Monitoreo.append(a)
        
        
        
        print ("****Access Control********")
        
        
        print ("****Política de Control de Acceso*********")
        
        a=int(input("Las políticas de control de acceso son desarrolladas y revisadas basadas en los requerimientos de seguridad del negocio?"))
        AccessControl.append(a)
        RequerimientosControlAcceso.append(a)
        a=int(input("Los controles de acceso tanto físico como lógico son tenidos en cuenta en las políticas de control de acceso?‎"))
        AccessControl.append(a) 
        RequerimientosControlAcceso.append(a)
        a=int(input("Tanto a los usuarios como a los proveedores de servicios se les dio una clara declaración de los requisitos de la empresa en cuanto a  control de acceso?‎"))
        AccessControl.append(a) 
        RequerimientosControlAcceso.append(a)
        
        
        print ("****Registración de Usuarios*********") 
        a=int(input("Existe algún procedimiento formal de altas/bajas de usuarios para acceder a los sistemas?"))
        AccessControl.append(a) 
        AdministracionUsuarios.append(a)

        print ("****Gestión de Privilegios*********")        
        a=int(input("La asignación y uso de privilegios en los sistemas de información, es restringida y controlada en base a las necesidades de uso y dichos privilegios son solo otorgados bajo un esquema formal de autorización?"))
        AccessControl.append(a)        
        AdministracionUsuarios.append(a)
        
        
        print ("****Administración de Contraseñas de Usuarios*********")        
        a=int(input("La asignación y reasignación de contraseñas debe controlarse a través de un proceso de gestión formal."))
        AccessControl.append(a)   
        AdministracionUsuarios.append(a)
        a=int(input("Se les solicita a los usuarios que firmen un acuerdo de confidencialidad del password?"))
        AccessControl.append(a)
        AdministracionUsuarios.append(a)
        
        print ("****Revisión de Roles de Usuarios*********")      
        a=int(input("Existe un proceso de revisión de privilegios y derechos de acceso a intervalos regulares. Por ejemplo: Privilegios especiales cada 3 meses, privilegios normales cada 6 meses?"))
        AccessControl.append(a) 
        AdministracionUsuarios.append(a)
        
        
        print ("****Uso de Password*********")
        a=int(input("Existe alguna práctica de seguridad en el sitio para guiar a la selección y mantenimiento de contraseñas seguras?"))
        AccessControl.append(a) 
        ResponsabilidadesUsuarios.append(a)
        
        print ("****Equipos desatendidos de Usuarios*********")
        a=int(input("Los usuarios y terceros son concientes de los requisitos de seguridad y procedimientos para proteger los equipos desatendidos? ‎Por ejemplo: Salir del sistema cuando las sesiones son terminadas o configurar terminación automática de sesiones por tiempo de inactividad, etc."))
        AccessControl.append(a) 
        ResponsabilidadesUsuarios.append(a)
        
                
        print ("****Política de Escritorio Limpio y Pantalla Limpia********")
        a=int(input("La organización ha adoptado una política de escritorio limpio con relación a los papeles y dispositivos de almacenamiento removibles?"))
        AccessControl.append(a) 
        ResponsabilidadesUsuarios.append(a)
        a=int(input("La organización ha adoptado una política de pantalla limpia con relación a los equipos de procesamiento de información?"))
        AccessControl.append(a)   
        ResponsabilidadesUsuarios.append(a)
        
        print ("****Políticas sobre Servicios de Red*******")  
        a=int(input("Se le provee a los usuarios acceso unicamente a los servicios de red a los cuales han sido autorizados específicamente?"))
        AccessControl.append(a)    
        ControlAccesoRed.append(a)
        a=int(input("Existen políticas de seguridad relacionadas con la red y los servicios de red?"))
        AccessControl.append(a) 
        ControlAccesoRed.append(a)
        
        print ("****Autenticaciones de Usuarios para conexiones externas*******")     
        a=int(input("Son utilizados mecanismos apropiados de autenticación para controlar el acceso remoto de los usuarios?"))
        AccessControl.append(a) 
        ControlAccesoRed.append(a)
        
        print ("****Identificación de equipamientos en la red*******")     
        a=int(input("Son considerados equipos de identificación automática para autenticar conexiones desde equips y direcciones específicas?"))
        AccessControl.append(a) 
        ControlAccesoRed.append(a)
        
        print ("****Diagnóstico Remoto y configuración de protección de puertos*******") 
        a=int(input("Los accesos físicos y lógicos a puertos de diagnóstico están apropiadamente controlados y protegidos por mecanismos de seguridad?"))
        AccessControl.append(a) 
        ControlAccesoRed.append(a)
        
        
        print ("****Segregación en la Red*******")
        a=int(input("Los grupos de servicios de información, usuarios y sistemas de información son segregados en la red?"))
        AccessControl.append(a) 
        ControlAccesoRed.append(a)
        a=int(input("La red (desde donde asociados de negocios o terceros necesitan acceder a los sistemas de información) es segregada utilizando mecanismos de seguridad perimetral como firewalls?‎"))
        AccessControl.append(a) 
        ControlAccesoRed.append(a)
        a=int(input("En la segregación de la red son hechas las consideraciones para separar las redes wireles en internas y privadas?"))
        AccessControl.append(a) 
        ControlAccesoRed.append(a)
        
        print ("****Control de Conexiones de Red*******")
        a=int(input("Existe una política de control de acceso que verifique conexiones provenientes de redes compartidas, especialmente aquellas que se extienden mas allá de los límites de la organización?"))
        AccessControl.append(a) 
        ControlAccesoRed.append(a)
        
        print ("****Control de Ruteo de Red*******")
        a=int(input("Existen políticas de control de acceso que establezcan los controles que deben ser realizados a los ruteos implementados en la red?"))
        AccessControl.append(a) 
        ControlAccesoRed.append(a)        
        a=int(input("Los controles de ruteo, están basados en mecanismos de identificación positiva de origen y destino?"))
        AccessControl.append(a) 
        ControlAccesoRed.append(a)
        
        print ("****Procedimientos de  log-on seguro*******")
        a=int(input("Los accesos a sistemas operativos son controlados por procedimientos de log-on seguro?"))
        AccessControl.append(a) 
        ControlesAccesoSistO.append(a)
        
        print ("****Identificación y Autenticación de Usuarios*******")
        a=int(input("Un único identificador de usuario (user ID) es proveído a cada usuario incluyendo operadores, administradores de sistemas y otros técnicos?"))
        AccessControl.append(a) 
        ControlesAccesoSistO.append(a)
        a=int(input("Se eligen adecuadas técnicas de autenticación para demostrar la identidad declarada de los usuarios?"))
        AccessControl.append(a) 
        ControlesAccesoSistO.append(a)
        a=int(input("El uso de cuentas de usuario genéricas son suministradas sólo en circunstancias especiales excepcionales, donde se especifícan los beneficios claros de su utilización. Controles adicionales pueden ser necesarios para mantener la seguridad."))
        AccessControl.append(a) 
        ControlesAccesoSistO.append(a)
        
        print ("****Gestión de Contraseñas*******")
        a=int(input("Existe un sistema de gestión de contraseñas que obliga al uso de controles como contraseña individual para auditoría, periodicidad de caducidad, complejidad mínima, almacenamiento encriptado, no despliegue de contraseñas por pantalla, etc.?"))
        AccessControl.append(a)
        ControlesAccesoSistO.append(a)
        
        print ("****Utilidades de Uso de Sistemas*******")
        a=int(input("En caso de existir programas utilitarios capaces de saltarse los controles de aplicaciones de los sistemas, estos están restringidos y bien controlados?"))
        AccessControl.append(a) 
        ControlesAccesoSistO.append(a)
        
        print ("****Expiración de Sesiones*******")
        a=int(input("Las aplicaciones son cerradas luego de un periodo determinado de inactividad?‎‎(Un tiempo determinado de inactividad puede ser determinado por algunos sistemas, que limpian la pantalla para prevenir acceso no autorizado, pero no cierra la aplicación o las sesiones de red)"))
        AccessControl.append(a) 
        ControlesAccesoSistO.append(a)
        
        print ("****Limitación de tiempo de conexión*******")
        a=int(input("Existen restricciones limitando el tiempo de conexión de aplicaciones de alto riesgo? Este tipo de configuraciones debe ser considerada para aplicaciones sensitivas cuyas terminales de acceso se encuentran en lugares de riesgo."))
        AccessControl.append(a) 
        ControlesAccesoSistO.append(a)
        
        print ("****Restricción de Acceso a la Información*******")
        a=int(input("El acceso a la información y los sistemas de aplicaciones por parte los usuarios y personal de soporte, está restringido en concordancia con las políticas de control de acceso definidas?"))
        AccessControl.append(a)
        ControlAccesoInformacion.append(a)
        
        print ("****Aislamiento de Sistemas Sensibles*******")
        a=int(input("Aquellos sistemas considerados sensibles, están en ambientes aislados, en computadoras dedicadas para el efecto, con recursos compartidos con aplicaciones seguras y confiables, etc?"))
        AccessControl.append(a) 
        ControlAccesoInformacion.append(a)
        
        print ("****Computación Móvil y Comunicaciones*******")
        a=int(input("Existe una política formal y medidas apropiadas de seguridad adoptadas para protegerse contra riesgo de utilización de computación móvil y equipos de comunicación?"))
        AccessControl.append(a) 
        ComputacionMovilTeletrabajo.append(a)
        a=int(input("Algunos ejemplos de computación móvil y equipos de telecomunicación incluyen: notebooks, palmtops, ‎laptops, smart cards, celulares. ‎"))
        AccessControl.append(a) 
        ComputacionMovilTeletrabajo.append(a)
        a=int(input("Son tenidos en cuenta los riesgos tales como trabajar en ambientes no protegidos en cuanto a las políticas de computación móvil?"))
        AccessControl.append(a) 
        ComputacionMovilTeletrabajo.append(a)
        
        print ("****Teletrabajo*******")
        a=int(input("Se desarrollan e implementan políticas, planes operativos y procedimientos con respecto a tareas de teletrabajo?"))
        AccessControl.append(a) 
        ComputacionMovilTeletrabajo.append(a)
        a=int(input("Las actividades de teletrabajo, son autorizadas y controladas por las gerencias y existen mecanismos adecuados de control para esta forma de trabajo?"))
        AccessControl.append(a) 
        ComputacionMovilTeletrabajo.append(a)
        
        print ("****Desarrollo, Adquisición y Mantenimiento de Sistemas de Información********")

        
        print ("****Análisis y Especificaciones de Rquerimientos de Seguridad******")
        a=int(input("Los requerimientos de seguridad para nuevos sistemas de información y fortalecimiento de los sistemas existentes, especifican los requerimientos para los controles de seguridad?"))
        DeAdManSistemas.append(a) 
        RequerimientosSeguridadInformacion.append(a)
        a=int(input("Los requerimientos y controles identificados reflejan el valor económico de los activos de información envueltos y las consecuencias de un fallo de seguridad?"))
        DeAdManSistemas.append(a) 
        RequerimientosSeguridadInformacion.append(a)
        a=int(input("Los requerimientos para la seguridad de información de los sistemas y prcesos para implementar dicha seguridad, son integrados en las primeras etapas de los proyectos de sistemas?"))
        DeAdManSistemas.append(a) 
        RequerimientosSeguridadInformacion.append(a)
        
        
        print ("****Validación de Datos de Entrada*******")
        a=int(input("Los datos introducidos a los sistemas, son validados para asegurar que son correctos y apropiados?"))
        DeAdManSistemas.append(a) 
        ProcesamientoAplicaciones.append(a)
        a=int(input("Los controles tales como: Diferentes tipos de mensajes de error para datos mal ingresados, Procedimientos para responder a los errores de validación, definición de responsabilidades para todo el personal envuelto en la carga de datos, etc. son considerados?"))
        DeAdManSistemas.append(a) 
        ProcesamientoAplicaciones.append(a)
        
        print ("****Control de Procesamiento Interno*******")
        a=int(input("Son incorporadas validaciones en las aplicaciones para detectar/prevenir que puedan ser ingresados datos no válidos por error o deliberadamente?"))
        DeAdManSistemas.append(a)
        ProcesamientoAplicaciones.append(a)
        a=int(input("Se tiene en cuenta en el diseño y la implementación de las aplicaciones que el riesgo de falllas en el procesamiento que conduzcan a perdida de integridad de datos sea minimizado?"))
        DeAdManSistemas.append(a) 
        ProcesamientoAplicaciones.append(a)
        
        print ("****Integridad de Mensajería*******")
        a=int(input("Los requerimientos para aseguramiento y protección de la integridad de los mensajes en las aplicaciones, son debidamente identificados e implementados los controles necesarios?"))
        DeAdManSistemas.append(a)
        ProcesamientoAplicaciones.append(a)
        a=int(input("Si una evaluación de riesgos de seguridad se llevó a cabo para determinar si es necesaria la integridad del mensaje, y para determinar el método más apropiado de aplicación."))
        DeAdManSistemas.append(a) 
        ProcesamientoAplicaciones.append(a)
        
        print ("****Validación de Datos de Salida*******")
        a=int(input("Los sistemas de aplicaciones de salida de datos, son validados para asegurar que el procesamiento de información almacenada sea correcta y apropiada a las circustancias?"))
        DeAdManSistemas.append(a)
        ProcesamientoAplicaciones.append(a)
        
        print ("****Políticas de Uso de Controles Criptográficos*******")
        a=int(input("La organización posee políticas de uso de controlec criptográficos para protección de la información? Estas políticas son implementadas con éxito?"))
        DeAdManSistemas.append(a)
        ControlesCriptograficos.append(a)
        a=int(input("La política criptográfica considera el enfoque de gestión hacia el uso de controles criptográficos, los resultados de la evaluación de riesgo para identificar nivel requerido de protección, gestión de claves y métodos de diversas normas para la aplicación efectiva?"))
        DeAdManSistemas.append(a)
        ControlesCriptograficos.append(a)
        
                
        print ("****Manejo de Claves*******")
        a=int(input("La administración de claves se utiliza efectivamente para apoyar el uso de técnicas criptográficas en la organización?"))
        DeAdManSistemas.append(a)
        ControlesCriptograficos.append(a)
        a=int(input("Las claves criptográficas están protegidas correctamente contra modificación, pérdida y/o destrucción?"))
        DeAdManSistemas.append(a)
        ControlesCriptograficos.append(a)
        a=int(input("Las claves públicas y privadas están protegidas contra divulgación no autorizada?"))
        DeAdManSistemas.append(a)
        ControlesCriptograficos.append(a)
        a=int(input("Los equipos utilizados para generar o almacenar claves, están físicamente protegidos?"))
        DeAdManSistemas.append(a)
        ControlesCriptograficos.append(a)
        a=int(input("Los sistemas de administración de claves, están basados en procedimientos estandarizados y seguros?"))
        DeAdManSistemas.append(a)
        ControlesCriptograficos.append(a)
        
        print ("****Control de Software Operativo*******")
        a=int(input("Existen procedimientos para controlar la instalación de software en los sistemas operativos (Esto es para minimizar el riesgo de corrupción de los sistemas operativos)"))
        DeAdManSistemas.append(a)
        SeguridadSistemas.append(a)
        
        print ("****Protección de Datos de Prueba de Sistemas*******")
        a=int(input("Los sistemas de testeo de datos, están debidamente protegidos y controlados? ‎La utilización de información personal o cualquier información sensitiva para propósitos de testeo, está prohibida?"))
        DeAdManSistemas.append(a)
        SeguridadSistemas.append(a)
        
        print ("****Control de Acceso a Código Fuente*******")
        a=int(input("Existen controles estrictos de modo a restringir el acceso al código fuente? (esto es para prevenir posibles cambios no autorizados)"))
        DeAdManSistemas.append(a)
        SeguridadSistemas.append(a)
        
        
        print ("****Procedimientos de Control de Cambios******")
        a=int(input("Existen procedimientos de control estricto con respecto a cambios en los sistemas de información? ‎‎(Esto es para minimizar la posible corrupción de los sistemas de información)‎‎"))
        DeAdManSistemas.append(a)
        SeguridadServiciosSoporte.append(a)
        a=int(input("Estos procedimientos aborda la necesidad de evaluación de riesgos, análisis de los impactos de los cambios?‎"))
        DeAdManSistemas.append(a)
        SeguridadServiciosSoporte.append(a)
        
        print ("****Revisión Técnica de Aplicaciones luego de Cambios en el Sistema Operativo*******")
        a=int(input("Existen procedimientos de control estricto con respecto a cambios en los sistemas de información? ‎‎(Esto es para minimizar la posible corrupción de los sistemas de información)‎"))
        DeAdManSistemas.append(a)
        SeguridadServiciosSoporte.append(a)
        
                
        print ("****Restricciones en Cambios de Paquetes de Software*******")
        a=int(input("Las modificaciones a los paquetes de software, son desalentadas o limitadas extrictamente a los cambios mínimos necesarios?‎"))
        DeAdManSistemas.append(a)
        SeguridadServiciosSoporte.append(a)
        a=int(input("Todos los cambios son estrictamente controlados?‎"))
        DeAdManSistemas.append(a)
        SeguridadServiciosSoporte.append(a)
        
        print ("****Fuga de Información*******")
        a=int(input("Existen controles para prevenir la fuga de información?‎"))
        DeAdManSistemas.append(a)
        SeguridadServiciosSoporte.append(a)
        a=int(input("Controles tales como escaneo de dispositivos de salida, monitoreo regular del personal y actividades permitidas en los sistemas bajo regulaciones locales, monitoreo de recursos, son considerados?‎"))
        DeAdManSistemas.append(a)
        SeguridadServiciosSoporte.append(a)
        
        print ("****Desarrollo de Software Tercerizado******")
        a=int(input("El desarrollo de software tercerizado, es supervisado y monitoreado por la organización?‎"))
        DeAdManSistemas.append(a)
        SeguridadServiciosSoporte.append(a)
        a=int(input("Puntos como: Adquisición de licencias, acuerdos de garantía, requerimientos contractuales de calidad asegurada, testeo antes de su instalación definitiva, revisión de código para prevenir troyanos, son considerados?‎"))
        DeAdManSistemas.append(a)
        SeguridadServiciosSoporte.append(a)
        
                
        print ("****Control de Vulnerabilidades Técnicas******")
        a=int(input("Se obtiene información oportuna en tiempo y forma sobre las vulnerabilidades técnicas de los sistemas de información que se utilizan?‎"))
        DeAdManSistemas.append(a)
        GestionVulnerabilidadesTecnicas.append(a)
        a=int(input("La organización evalúa e implementa medidas apropiadas de mitigación de riesgos a las vulnerabilidades a las que está expuesta?‎"))
        DeAdManSistemas.append(a)
        GestionVulnerabilidadesTecnicas.append(a)
        
        print ("****Gestión de Incidentes de Seguridad de Información********")

        
        print ("****Reportando Eventos de Seguridad de la Información******")
        a=int(input("Los eventos de seguridad de información, son reportados a través de los canales correspondientes lo más rápido posible?‎"))
        GestionIncidentes.append(a)
        ReportandoVulnerabilidades.append(a)
        a=int(input("Son desarrollados e implementados procedimientos formales de reporte, respuesta y escalación en incidentes de seguridad?‎"))
        GestionIncidentes.append(a)
        ReportandoVulnerabilidades.append(a)
        
        print ("****Reportando Vulnerabilidaes de la Seguridad******")
        a=int(input("Existen procedimientos que aseguren que todos los empleados deben reportar cualquier vulnerabilidad en la seguridad en los servicios o sistemas de información?‎"))
        GestionIncidentes.append(a)
        ReportandoVulnerabilidades.append(a)

        print ("****Responsabilidades y Procedimientos******")
        a=int(input("Están claramente establecidos los procedimientos y responsabilidades de gestión para asegurar una rápida, efectiva y ordenada respuesta a los incidentes de seguridad de información?‎"))
        GestionIncidentes.append(a)
        GestionProcesoMejoras.append(a)
        a=int(input("Es utilizado el monitoreo de sistemas, alertas y vulnerabilidades para detectar incidentes de seguridad?‎"))
        GestionIncidentes.append(a)    
        GestionProcesoMejoras.append(a)
        a=int(input("Los objetivos de la gestión de incidentes de seguridad de información, están acordados con las gerencias?‎"))
        GestionIncidentes.append(a)      
        GestionProcesoMejoras.append(a)


        print ("****Aprendiendo de los Incidentes de Seguridad de la Información******")
        a=int(input("Existen mecanismos establecidos para identificar y cuantificar el tipo, volumen y costo de los incidentes de seguridad?‎"))
        GestionIncidentes.append(a)
        GestionProcesoMejoras.append(a)
        a=int(input("La información obtenida de la evaluación de incidentes de seguridad que ocurrieron en el pasado, es utilizada para determinar el impacto recurrente de incidencia  y corregir errores?‎"))
        GestionIncidentes.append(a)    
        GestionProcesoMejoras.append(a)

        print ("****Recolección de Evidencia******")
        a=int(input("Si las medidas de seguimiento contra una persona u organización después de un incidente de seguridad de la información implica una acción legal (ya sea civil o penal)‎"))
        GestionIncidentes.append(a)
        GestionProcesoMejoras.append(a)
        a=int(input("Las evidencias relacionadas con incidentes, son recolectadas, retenidas y presentadas conforme las disposiciones legales vigentes en las jurisdicciones pertinentes?‎"))
        GestionIncidentes.append(a) 
        GestionProcesoMejoras.append(a)
        a=int(input("Los procedimientos internos son desarrollados y seguidos al pié de la letra cuando se debe recolectar y presentar evidencia para propósitos disciplinarios dentro de la organización?‎"))
        GestionIncidentes.append(a)  
        GestionProcesoMejoras.append(a)
        
        print ("****Gestión de la Continuidad del Negocio******")

        print ("****Incluyendo Seguridad en el Proceso de Gestión de Continuidad del Negocio******")
        a=int(input("Existen procesos que direccionan los requerimientos de seguridad de información para el desarrollo y mantenimiento de la Continuidad del Negocio dentro de la Organización?‎"))
        GestionContinuidad.append(a)
        AspectosContinuidadNegocio.append(a)
        a=int(input("Estos procesos, entienden cuales son los riesgos que la organización enfrenta, identifican los activos críticos, los impactos de los incidentes, consideran la implementación de controles preventivos adicionales y la documentación de los Planes de Continuidad del Negocio direccionando los requerimientos de seguridad?‎"))
        GestionContinuidad.append(a)    
        AspectosContinuidadNegocio.append(a)
        
        print ("****Continuidad del Negocio y Evaluación de Riesgos******")
        a=int(input("Los eventos que puedan causar interrupción al negocio, son identificados sobre la base de probabilidad, impacto y posibles consecuencias para la seguridad de información?‎"))
        GestionContinuidad.append(a) 
        AspectosContinuidadNegocio.append(a)
        
        
        print ("****Desarrollo e Implementación de Planes de Continuidad incluyendo Seguridad de la Información******")
        a=int(input("Existen procesos que direccionan los requerimientos de seguridad de información para el desarrollo y mantenimiento de la Continuidad del Negocio dentro de la Organización?‎"))
        GestionContinuidad.append(a)
        AspectosContinuidadNegocio.append(a)
        a=int(input("Estos procesos, entienden cuales son los riesgos que la organización enfrenta, identifican los activos críticos, los impactos de los incidentes, consideran la implementación de controles preventivos adicionales y la documentación de los Planes de Continuidad del Negocio direccionando los requerimientos de seguridad?‎"))
        GestionContinuidad.append(a)  
        AspectosContinuidadNegocio.append(a)          
        
        print ("****Business continuity planning framework******")
        a=int(input("Existe un marco único del Plan de Continuidad de Negocios?‎"))
        GestionContinuidad.append(a)        
        AspectosContinuidadNegocio.append(a)
        a=int(input("Este marco, es mantenido regularmente para asegurarse que todos los planes son consistentes e identifican prioridades para testeo y mantenimiento?‎"))
        GestionContinuidad.append(a) 
        AspectosContinuidadNegocio.append(a)
        a=int(input("El Plan de Continuidad del Negocio direccionan los requerimientos de seguridad de información identificados?‎"))
        GestionContinuidad.append(a) 
        AspectosContinuidadNegocio.append(a)
        
        
        print ("****Desarrollo e Implementación de Planes de Continuidad incluyendo Seguridad de la Información******")
        a=int(input("Existen procesos que direccionan los requerimientos de seguridad de información para el desarrollo y mantenimiento de la Continuidad del Negocio dentro de la Organización?‎"))
        GestionContinuidad.append(a)
        AspectosContinuidadNegocio.append(a)
        a=int(input("Estos procesos, entienden cuales son los riesgos que la organización enfrenta, identifican los activos críticos, los impactos de los incidentes, consideran la implementación de controles preventivos adicionales y la documentación de los Planes de Continuidad del Negocio direccionando los requerimientos de seguridad?‎"))
        GestionContinuidad.append(a)     
        AspectosContinuidadNegocio.append(a)
        
        print ("****Business continuity planning framework******")
        a=int(input("Existe un marco único del Plan de Continuidad de Negocios?‎"))
        GestionContinuidad.append(a)
        AspectosContinuidadNegocio.append(a)
        a=int(input("Este marco, es mantenido regularmente para asegurarse que todos los planes son consistentes e identifican prioridades para testeo y mantenimiento?‎"))
        GestionContinuidad.append(a)   
        AspectosContinuidadNegocio.append(a)
        a=int(input("El Plan de Continuidad del Negocio direccionan los requerimientos de seguridad de información identificados?‎"))
        GestionContinuidad.append(a)  
        AspectosContinuidadNegocio.append(a)
        
        print ("****Prueba, Mantenimiento y Reevaluando Planes de Continuidad del Negocio ******")
        a=int(input("Los Planes de Continuidad del Negocio, son probados regularmente para asegurarse de que están actualizados y son efectivos?‎"))
        GestionContinuidad.append(a)
        AspectosContinuidadNegocio.append(a)
        a=int(input("Los tests de planes de continuidad de negocio, aseguran que todos los miembros del equipo de recuperación y otros equipos relevantes sean advertidos del contenido y sus responsabilidades para la continuidad del negocio y la seguridad de información, son concientes de sus roles y funciones dentro del plan cuando este se ejecuta?‎"))
        GestionContinuidad.append(a)  
        AspectosContinuidadNegocio.append(a)

        print ("****Cumplimiento ******")        
      
        print ("****Identificación de Legislación Aplicable ******")
        a=int(input("Todas las leyes relevantes, regulaciones, requerimientos contractuales y organizacionales son tenidos en cuenta de modo a que estén documentados para cada sistema de información en la organización?‎"))
        Cumplimiento.append(a)
        CumplimientoLegales.append(a)
        a=int(input("Los controles específicos y responsabilidades individuales de modo a cumplir con estos requerimientos, son debidamente definidos y documentados?‎"))
        Cumplimiento.append(a)
        CumplimientoLegales.append(a)

        print ("****Derechos de Propiedad Intelectual******")
        a=int(input("Existen procedimientos para asegurar el cumplimiento de los requerimientos legales, regulatorios y contractuales sobre el uso de materiales y software que estén protegidos por derechos de propiedad intelectual?‎"))
        Cumplimiento.append(a)
        CumplimientoLegales.append(a)
        a=int(input("Estos procedimientos, están bien implementados?‎"))
        Cumplimiento.append(a)
        CumplimientoLegales.append(a)
        a=int(input("Controles tales como: Política de Cumplimiento de Derechos de Propiedad Intelectual, Procedimientos de Adquisición de Software, Política de concientización, Mantenimiento de Prueba de la Propiedad, Cumplimiento con Términos y Condiciones, son consideradas?‎"))
        Cumplimiento.append(a)  
        CumplimientoLegales.append(a)

        print ("****Protección de los Registros de la Organización******")
        a=int(input("Los registros importantes de la organización están protegidos contra pérdida, destrucción y falsificación en concordancia con los requerimientos legales, regulatorios, contractuales y de negocio?‎"))
        Cumplimiento.append(a)
        CumplimientoLegales.append(a)
        a=int(input("Están previstas las consideraciónes con respecto al posible deterioro de medios de almacenamiento utilizados para almacenar registros?‎"))
        Cumplimiento.append(a)
        CumplimientoLegales.append(a)
        a=int(input("Los sistemas de almacenamiento son elegidos de modo a que los datos requeridos puedan ser recuperados en un rango de tiempo aceptable y en el formato necesario, dependiendo de los requerimientos a ser cumplidos?‎"))
        Cumplimiento.append(a)  
        CumplimientoLegales.append(a)


        print ("****Protección de los Datos y privacidad de los datos personales******")
        a=int(input("La protección de los datos y la privacidad, están asegurados por legislaciones relevantes, regulaciones y si son aplicables, por cláusulas contractuales?‎"))
        Cumplimiento.append(a)
        CumplimientoLegales.append(a)
        
        
        print ("****Prevención del maluso de las instalaciones de procesamiento******")
        a=int(input("El uso de instalaciones de proceso de información para cualquier propósito no autorizado o que no sea del negocio, sin la aprobación pertinente, es tratada como utilización impropia de las instalaciones?‎"))
        Cumplimiento.append(a)
        CumplimientoLegales.append(a)
        a=int(input("Los mensajes de alerta de ingreso, son desplegados antes de permitir el ingreso a la red o a los sistemas?   El usuario tiene conocimiento de las alertas y reacciona apropiadamente al mensaje en pantalla?‎"))
        Cumplimiento.append(a)
        CumplimientoLegales.append(a)
        a=int(input("Es realizado un asesoramiento jurídico, antes de aplicar cualquier procedimiento de monitoreo y control?‎"))
        Cumplimiento.append(a)   
        CumplimientoLegales.append(a)

        print ("****Regulación de Controles Criptográficos******")
        a=int(input("Los controles criptográficos son usados en cumplimiento de los acuerdos contractuales establecidos, leyes y regulaciones?‎"))
        Cumplimiento.append(a)
        CumplimientoLegales.append(a)
        
        print ("****Cumplimiento con Políticas de Seguridad y Estándares******")       
        a=int(input("Los Administradores se aseguran que todos los procedimientos dentro de su area de responsabilidad, se llevan a cabo correctamente para lograrl el cumplimiento de las normas y políticas de seguridad?‎"))
        Cumplimiento.append(a)
        CumplimientoRegulacionesTecnicas.append(a)
        a=int(input("Los Administradores, revisan regularmente el cumplimiento de las instalaciones de procesamiento de información dentro del area de su responsabilidad de modo a cumplir con los procedimientos y políticas de seguridad pertinentes?‎"))
        Cumplimiento.append(a)   
        CumplimientoRegulacionesTecnicas.append(a)
      
        print ("****Chequeo de Cumplimiento Técnico******")       
        a=int(input("Los sistemas de información son regularmente revisados con respecto al cumplimiento de estándares de seguridad?‎"))
        Cumplimiento.append(a)
        CumplimientoRegulacionesTecnicas.append(a)
        a=int(input("La verificación técnica es llevada a cabo por, o bajo la supervisión de, personal técnico competente y autorizado?‎"))
        Cumplimiento.append(a)   
        CumplimientoRegulacionesTecnicas.append(a)
        
        print ("****Controles de Auditoría de los Sistemas de Información******")       
        a=int(input("Los requerimientos y actividades de auditoría, incluyen verificación de sistemas de información  que fueron previamente planeados cuidadosamente de modo a minimizar los riesgos de interrupciones en el proceso de negocio? ‎"))
        Cumplimiento.append(a)
        ConsideracionesSistemas.append(a)
        a=int(input("Los requerimientos de auditoria son alcanzables y de acuerdo con una gestión adecuada?‎"))
        Cumplimiento.append(a)   
        ConsideracionesSistemas.append(a)

        print ("****Protección de la información contra las heramientas de auditoría******")       
        a=int(input("La información a la que se accede por medio de las herramientas de auditoría, ya sean software o archivos de datos, están protegidos para prevenir el mal uso o fuga no autorizada? ‎"))
        Cumplimiento.append(a)
        ConsideracionesSistemas.append(a)
        a=int(input("El ambiente de auditoría está separado de los ambientes operacionales y de desarrollo, a penos que haya un nivel apropiado de protección?‎"))
        Cumplimiento.append(a) 
        ConsideracionesSistemas.append(a)
        
        pPoliticasSeguridad = statistics.mean(PoliticasSeguridad)
        
        pOrganizationSeguridad = statistics.mean(OrganizationSeguridad)
        pOrganizacionInterna = statistics.mean(OrganizacionInterna)
        pPartesExternas  = statistics.mean(PartesExternas)
        
        
        
        pAdministracionActivos = statistics.mean(AdministracionActivos)
        pResponsibilidadActivos = statistics.mean(PartesExternas)
        pClasificacionInformacion = statistics.mean(ClasificacionInformacion)
        
        pSeguridadRH = statistics.mean(SeguridadRH)
        pPrevioEmpleo = statistics.mean(PrevioEmpleo)
        pDuranteEmpleo = statistics.mean(DuranteEmpleo)
        pTerminacionEmpleo = statistics.mean(TerminacionEmpleo)
        
        pSeguridadFA = statistics.mean(SeguridadFA)
        pAreasSegura = statistics.mean(AreasSegura)
        pEquipamientoSeguridad = statistics.mean(EquipamientoSeguridad)
        
        
        pComunicacionesOperaciones = statistics.mean(ComunicacionesOperaciones)
        pProcedimientosOperativas = statistics.mean(ProcedimientosOperativas)
        pManejoTercerizados = statistics.mean(ManejoTercerizados)
        pPlaneamientoSistemas = statistics.mean(PlaneamientoSistemas)
        pProteccionMovil = statistics.mean(ProteccionMovil)
        pCopiasRespaldo = statistics.mean(CopiasRespaldo)
        pAdministracionRed = statistics.mean(AdministracionRed)
        pManejoMedios = statistics.mean(ManejoMedios)
        pIntercambioInformacion = statistics.mean(IntercambioInformacion)
        pServiciosElectronico = statistics.mean(ServiciosElectronico)
        pMonitoreo = statistics.mean(Monitoreo)
        
        pAccessControl = statistics.mean(AccessControl)
        pRequerimientosControlAcceso = statistics.mean(RequerimientosControlAcceso)
        pAdministracionUsuarios = statistics.mean(AdministracionUsuarios)
        pResponsabilidadesUsuarios = statistics.mean(ResponsabilidadesUsuarios)
        pControlAccesoRed = statistics.mean(ControlAccesoRed)
        pControlesAccesoSistO = statistics.mean(ControlesAccesoSistO)
        pControlAccesoInformacion = statistics.mean(ControlAccesoInformacion)	
        pComputacionMovilTeletrabajo = statistics.mean(ComputacionMovilTeletrabajo)
        

        pDeAdManSistemas= statistics.mean(DeAdManSistemas)		
        pRequerimientosSeguridadInformacion = statistics.mean(RequerimientosSeguridadInformacion)	
        pProcesamientoAplicaciones = statistics.mean(ProcesamientoAplicaciones)		
        pControlesCriptograficos	= statistics.mean(ControlesCriptograficos)
        pSeguridadSistemas = statistics.mean(SeguridadSistemas)
        pSeguridadServiciosSoporte = statistics.mean(SeguridadServiciosSoporte)
        pGestionVulnerabilidadesTecnicas = statistics.mean(GestionVulnerabilidadesTecnicas)
        		
        pGestionIncidentes = statistics.mean(GestionIncidentes)	
        pReportandoVulnerabilidades = statistics.mean(ReportandoVulnerabilidades)		
        pGestionProcesoMejoras = statistics.mean(GestionProcesoMejoras)	
        
        
        pGestionContinuidad = statistics.mean(GestionContinuidad)
        pAspectosContinuidadNegocio = statistics.mean(AspectosContinuidadNegocio)
        
        pCumplimiento = statistics.mean(Cumplimiento)		
        pCumplimientoLegales = statistics.mean(CumplimientoLegales)	
        pCumplimientoRegulacionesTecnicas = statistics.mean(CumplimientoRegulacionesTecnicas)
        pConsideracionesSistemas = statistics.mean(ConsideracionesSistemas)

    

        
    elif opcionMenu=="2": 
       
        CumplimientoControl = { 
        'titulos' : ["Política de Seguridad	",
                     "Políticas de Seguridad de Información",
                     "Organization de la Seguridad de Información",
                     "Organizacion Interna",
                     "Partes Externas",
                     "Administración de Activos	",
                     "Responsibilidad por Activos",
                     "Clasificación de la Información",
                     "Seguridad de Recursos Humanos	",
                     "Previo al Empleo",
                     "Durante el Empleo	 ",
                     "Terminación o Cambio de Empleo",
                     "Seguridad Física y Ambiental",
                     "Areas Seguras	 ",
                     "Equipamiento de Seguridad	",
                     "Gestión de Comunicaciones y Operaciones",
                     "Procedimientos y Responsabilidades Operativas",
                     "Manejo de Entrega de Servicios Tercerizados",
                     "Planeamiento y Aceptacion de Sistemas",
                     "Protección contra código malicioso y móvil",
                     "Copias de Respaldo",
                     "Administración de la Seguridad de la Red",
                     "Manejo de Medios",
                     "Intercambio de Información",
                     "Servicios de Comercio Electrónico	",
                     "Monitoreo ",
                     "Access Control",
                     "Requerimientos del Negocio para Control de Acceso",
                     "Administración de Accesos de Usuarios	",
                     "Responsabilidades de Usuarios",
                     "Control de Acceso a la Red",
                     "Controles de Acceso a Sistemas Operativos	",
                     "Control de Acceso a las Aplicaciones y a la Información",
                     "Computación Móvil y Teletrabajo", 
                     "Desarrollo, Adquisición y Mantenimiento de Sistemas de Información",
                     "Requerimientos de Seguridad de los Sistemas de Información",
                     "Procesamiento Correcto en Aplicaciones",
                     "Controles Criptográficos	",
                     "Seguridad de los Archivos de Sistemas",
                     "Seguridad en el Desarrollo y Servicios de Soporte	",
                     "Gestión de Vulnerabilidades Técnicas",
                     "Gestión de Incidentes de Seguridad de Información	"
                     "Reportando Eventos de Seguridad y Vulnerabilidades",
                     "Gestión de Incidentes de Seguridad de la Información y Proceso de Mejoras	",
                     "Gestión de la Continuidad del Negocio",
                     "Aspectos de Seguridad en la Gestión de la Continuidad del Negocio	",
                     "Cumplimiento",
                     "Cumplimiento con Requerimientos Legales",
                     "Cumplimiento con las políticas, estándares y regulaciones técnicas",
                     "Consideraciones de Auditoría de Sistemas"
                     ],
    'datos' : [pPoliticasSeguridad,
                 pPoliticasSeguridad,
                 pOrganizationSeguridad,
                 pOrganizacionInterna,
                 pPartesExternas,
                 pAdministracionActivos,
                 pResponsibilidadActivos,
                 pClasificacionInformacion,
                 pSeguridadRH,
                 pPrevioEmpleo,
                 pDuranteEmpleo,
                 pTerminacionEmpleo,
                 pSeguridadFA,
                 pAreasSegura,
                 pEquipamientoSeguridad,
                 pComunicacionesOperaciones, 
                 pProcedimientosOperativas,
                 pManejoTercerizados,
                 pPlaneamientoSistemas,
                 pProteccionMovil,
                 pCopiasRespaldo,
                 pAdministracionRed, 
                 pManejoMedios,
                 pIntercambioInformacion,
                 pServiciosElectronico,
                 pMonitoreo,
                 pAccessControl, 
                 pRequerimientosControlAcceso, 
                 pAdministracionUsuarios,
                 pResponsabilidadesUsuarios, 
                 pControlAccesoRed,
                 pControlesAccesoSistO,
                 pControlAccesoInformacion,
                 pComputacionMovilTeletrabajo,
                 pDeAdManSistemas,
                 pRequerimientosSeguridadInformacion,
                 pProcesamientoAplicaciones,		
                 pControlesCriptograficos,
                 pSeguridadSistemas,
                 pSeguridadServiciosSoporte,
                 pGestionVulnerabilidadesTecnicas,
                 pDeAdManSistemas,
                 pReportandoVulnerabilidades,
                 pGestionProcesoMejoras,
                 pGestionContinuidad,
                 pAspectosContinuidadNegocio,
                 pCumplimientoLegales, 
                 pCumplimientoRegulacionesTecnicas,
                 pConsideracionesSistemas
                 ]
    
        }
        
        promedios_dataframe = pd.DataFrame(CumplimientoControl)
        print (promedios_dataframe)
        
    elif opcionMenu=="4":
        print ("")
        etiquetas = ["Políticas de Seguridad ",
                     "Seguridad de Información",
                     "Administración de Activos",
                     "Seguridad de Recursos Humanos",
                     "Seguridad Física y Ambiental",
                     "Gestión de Comunicaciones y Operaciones ",
                     "Access Control ",
                     "Desarrollo, Adquisición y Mantenimiento  ",
                     "Gestión de Incidentes de Seguridad de Información	 ",
                     "Gestión de la Continuidad del Negocio ",
                     "Cumplimiento"
                     ]
        
        datos = [pPoliticasSeguridad, 
                 pOrganizationSeguridad,
                 pAdministracionActivos,
                 pSeguridadRH,
                 pSeguridadFA,
                 pComunicacionesOperaciones,
                 pAccessControl,
                 pDeAdManSistemas,
                 pGestionIncidentes,
                 pGestionContinuidad,
                 pCumplimiento  
                 ]
        
     
        plot_bar_x()
        
    elif opcionMenu=="3":
        print ("")
        promediosTot = { 
    
    'titulos': ["Políticas de Seguridad ",
                     "Seguridad de Información",
                     "Administración de Activos",
                     "Seguridad de Recursos Humanos",
                     "Seguridad Física y Ambiental",
                     "Gestión de Comunicaciones y Operaciones ",
                     "Access Control ",
                     "Desarrollo, Adquisición y Mantenimiento  ",
                     "Gestión de Incidentes de Seguridad de Información	 ",
                     "Gestión de la Continuidad del Negocio ",
                     "Cumplimiento"
                     ],
    'datos': [pPoliticasSeguridad, 
                 pOrganizationSeguridad,
                 pAdministracionActivos,
                 pSeguridadRH,
                 pSeguridadFA,
                 pComunicacionesOperaciones,
                 pAccessControl,
                 pDeAdManSistemas,
                 pGestionIncidentes,
                 pGestionContinuidad,
                 pCumplimiento  
                 ]
    }
    
        promedios_dataframe = pd.DataFrame(promediosTot)
        print (promedios_dataframe)
    
    elif opcionMenu == "5":
        for i in PoliticasSeguridad:
            if i < 25:
                valores25 = valores25 + 1
            elif i < 26 & i > 75:
                valores75 = valores75 + 1
            elif i < 76 & i > 100:
                valores100 = valores100 + 1
                print (valores25, valores75, valores100)
    elif opcionMenu=="9":
        break
    else:
        print ("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
        

 
 