# 📅 Agenda Moderna

Una aplicación de agenda personal moderna y minimalista desarrollada con Python y Tkinter.

## ✨ Características

### 🎨 Diseño Moderno
- **Tema oscuro** con paleta de colores moderna
- **Interfaz minimalista** y limpia
- **Tipografía Segoe UI** para mejor legibilidad
- **Componentes con estilo** tipo Material Design

### 📋 Funcionalidades Principales
- **Gestión de eventos** con fecha, hora y descripción
- **Calendario interactivo** para selección de fechas
- **Recordatorios organizados** en lista visual
- **Búsqueda de eventos** en tiempo real
- **Validación de datos** automática
- **Persistencia de datos** en formato JSON


## 🚀 Instalación

1. **Clona o descarga** el proyecto
2. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Ejecuta la aplicación**:
   ```bash
   python main.py
   ```

## 📦 Dependencias

- Python 3.7+
- tkinter (incluido con Python)
- tkcalendar

## 🎯 Uso

### Pantalla Principal
- **Reloj digital** que se actualiza en tiempo real
- **Fecha actual** con día de la semana en español
- **Botones principales** para acceder a funciones

### Crear Eventos
1. Haz clic en "📅 Gestionar Calendario"
2. Completa el formulario:
   - Fecha del evento
   - Tipo de evento (desplegable)
   - Nombre descriptivo
   - Hora de inicio y fin
   - Descripción opcional
3. Haz clic en "💾 Guardar Evento"

### Ver Recordatorios
1. Haz clic en "🔔 Ver Recordatorios"
2. Usa la **barra de búsqueda** para filtrar eventos
3. Selecciona eventos para **eliminar** o **editar**
4. Ve el **estado** de cada evento (Pasado, Hoy, Mañana, Futuro)

## 🎨 Paleta de Colores

La aplicación utiliza una paleta moderna con:
- **Fondo**: Negro profundo (#0F0F0F)
- **Superficies**: Grises oscuros (#1A1A1A, #2D2D2D)
- **Primario**: Índigo moderno (#6366F1)
- **Secundario**: Verde esmeralda (#10B981)
- **Acentos**: Ámbar (#F59E0B), Rojo (#EF4444)

## 📁 Estructura de Archivos

```
Agenda-main/
├── main.py              # Aplicación principal
├── requirements.txt     # Dependencias
├── eventos.json         # Datos de eventos (se crea automáticamente)
├── recordatorio.txt     # Datos antiguos (compatibilidad)
└── README.md           # Este archivo
```

## 🔄 Migración de Datos

La aplicación es **compatible** con el formato anterior:
- Los eventos antiguos (formato texto) se siguen mostrando
- Los nuevos eventos se guardan en formato JSON
- Ambos formatos coexisten sin problemas

**Disfruta organizando tu tiempo con estilo! 🎯**
