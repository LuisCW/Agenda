from datetime import datetime, date, timedelta
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from tkinter import simpledialog
from tkcalendar import Calendar, DateEntry
import tkinter as tk
from tkinter import font as tkFont
import time
import json
import os
import csv

# Lista global para eventos
lista = []

# Paleta de colores moderna y minimalista expandida
class ModernColors:
    # Colores principales (Dark theme premium)
    BACKGROUND = "#0B0B0F"          # Negro profundo premium
    SURFACE = "#1A1A23"             # Gris muy oscuro con tinte azul
    SURFACE_VARIANT = "#2D2D3A"     # Gris oscuro premium
    SURFACE_ELEVATED = "#25253A"    # Superficie elevada
    CARD_BACKGROUND = "#1E1E2E"     # Fondo de tarjetas
    
    # Colores primarios con gradientes
    PRIMARY = "#6366F1"             # Índigo moderno
    PRIMARY_VARIANT = "#4F46E5"     # Índigo oscuro
    PRIMARY_LIGHT = "#818CF8"       # Índigo claro
    PRIMARY_GRADIENT_START = "#6366F1"
    PRIMARY_GRADIENT_END = "#8B5CF6"
    
    # Colores secundarios
    SECONDARY = "#10B981"           # Verde esmeralda
    SECONDARY_VARIANT = "#059669"   # Verde oscuro
    SECONDARY_LIGHT = "#34D399"     # Verde claro
    
    # Colores de acento
    ACCENT = "#F59E0B"              # Ámbar
    ACCENT_VARIANT = "#D97706"      # Ámbar oscuro
    ERROR = "#EF4444"               # Rojo moderno
    WARNING = "#F97316"             # Naranja
    SUCCESS = "#22C55E"             # Verde
    INFO = "#3B82F6"                # Azul información
    
    # Texto mejorado
    TEXT_PRIMARY = "#FFFFFF"        # Blanco puro
    TEXT_SECONDARY = "#E4E4E7"      # Gris muy claro
    TEXT_TERTIARY = "#A1A1AA"       # Gris claro
    TEXT_MUTED = "#71717A"          # Gris medio
    TEXT_DISABLED = "#52525B"       # Gris oscuro
    
    # Bordes y divisores mejorados
    BORDER = "#3F3F46"              # Borde sutil
    BORDER_LIGHT = "#52525B"        # Borde más visible
    DIVIDER = "#27272A"             # Divisor sutil
    DIVIDER_STRONG = "#3F3F46"      # Divisor más visible
    
    # Estados de hover y focus
    HOVER_OVERLAY = "#FFFFFF10"     # Overlay blanco translúcido
    FOCUS_RING = "#6366F150"        # Anillo de enfoque
    SELECTION = "#6366F130"         # Color de selección
    
    # Sombras (colores sólidos para tkinter)
    SHADOW_LIGHT = "#1A1A1A"
    SHADOW_MEDIUM = "#2A2A2A"
    SHADOW_STRONG = "#3A3A3A"

class ModernStyleUtils:
    @staticmethod
    def configure_modern_style():
        """Configura el estilo moderno para toda la aplicación"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configurar estilos para botones principales
        style.configure("Modern.TButton",
                       background=ModernColors.PRIMARY,
                       foreground=ModernColors.TEXT_PRIMARY,
                       borderwidth=0,
                       focuscolor='none',
                       font=("Segoe UI", 12, "normal"),
                       padding=(24, 14))
        
        style.map("Modern.TButton",
                 background=[("active", ModernColors.PRIMARY_VARIANT),
                           ("pressed", ModernColors.PRIMARY_VARIANT)],
                 relief=[("pressed", "flat"), ("!pressed", "flat")])
        
        # Estilo para botones secundarios mejorado
        style.configure("Secondary.TButton",
                       background=ModernColors.SURFACE_VARIANT,
                       foreground=ModernColors.TEXT_SECONDARY,
                       borderwidth=1,
                       focuscolor='none',
                       font=("Segoe UI", 11, "normal"),
                       padding=(20, 10))
        
        style.map("Secondary.TButton",
                 background=[("active", ModernColors.SURFACE_ELEVATED),
                           ("pressed", ModernColors.SURFACE_ELEVATED)])
        
        # Estilo para entradas de texto mejorado
        style.configure("Modern.TEntry",
                       fieldbackground=ModernColors.SURFACE_VARIANT,
                       foreground=ModernColors.TEXT_PRIMARY,
                       borderwidth=2,
                       insertcolor=ModernColors.PRIMARY,
                       font=("Segoe UI", 12),
                       padding=12)
        
        style.map("Modern.TEntry",
                 focuscolor=[("focus", ModernColors.PRIMARY)],
                 bordercolor=[("focus", ModernColors.PRIMARY)])
        
        # Estilo para combobox mejorado
        style.configure("Modern.TCombobox",
                       fieldbackground=ModernColors.SURFACE_VARIANT,
                       foreground=ModernColors.TEXT_PRIMARY,
                       borderwidth=2,
                       font=("Segoe UI", 12),
                       padding=12)
        
        style.map("Modern.TCombobox",
                 focuscolor=[("focus", ModernColors.PRIMARY)],
                 bordercolor=[("focus", ModernColors.PRIMARY)])
        
        # Estilo para Treeview
        style.configure("Modern.Treeview",
                       background=ModernColors.SURFACE,
                       foreground=ModernColors.TEXT_PRIMARY,
                       fieldbackground=ModernColors.SURFACE,
                       borderwidth=0,
                       font=("Segoe UI", 11))
        
        style.configure("Modern.Treeview.Heading",
                       background=ModernColors.SURFACE_VARIANT,
                       foreground=ModernColors.TEXT_PRIMARY,
                       font=("Segoe UI", 11, "bold"),
                       padding=10)
        
        style.map("Modern.Treeview",
                 background=[("selected", ModernColors.PRIMARY)],
                 foreground=[("selected", ModernColors.TEXT_PRIMARY)])
    
    @staticmethod
    def create_gradient_button(parent, text, command, icon="", bg_start=None, bg_end=None, width=300, height=50):
        """Crea un botón con efecto de gradiente simulado"""
        if bg_start is None:
            bg_start = ModernColors.PRIMARY
        if bg_end is None:
            bg_end = ModernColors.PRIMARY_VARIANT
            
        # Frame contenedor para el efecto de gradiente
        button_frame = tk.Frame(parent, bg=ModernColors.SURFACE, bd=0)
        
        # Canvas para crear el efecto de gradiente
        canvas = tk.Canvas(button_frame, width=width, height=height, 
                          bg=bg_start, bd=0, highlightthickness=0)
        canvas.pack()
        
        # Botón principal
        button = tk.Button(canvas,
                          text=f"{icon} {text}",
                          command=command,
                          bg=bg_start,
                          fg=ModernColors.TEXT_PRIMARY,
                          font=("Segoe UI", 13, "normal"),
                          bd=0,
                          padx=30,
                          pady=15,
                          cursor="hand2",
                          activebackground=bg_end,
                          activeforeground=ModernColors.TEXT_PRIMARY)
        
        # Centrar el botón en el canvas
        canvas.create_window(width/2, height/2, window=button)
        
        # Efectos de hover
        def on_enter(event):
            button.configure(bg=bg_end)
            canvas.configure(bg=bg_end)
        
        def on_leave(event):
            button.configure(bg=bg_start)
            canvas.configure(bg=bg_start)
        
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
        canvas.bind("<Enter>", on_enter)
        canvas.bind("<Leave>", on_leave)
        
        return button_frame
    
    @staticmethod
    def create_card_frame(parent, padding=20, elevation=2):
        """Crea un marco tipo tarjeta con sombra simulada"""
        # Frame principal para la sombra
        shadow_frame = tk.Frame(parent, bg=ModernColors.SHADOW_MEDIUM, bd=0)
        
        # Frame de la tarjeta
        card_frame = tk.Frame(shadow_frame, bg=ModernColors.CARD_BACKGROUND, 
                             bd=0, relief="flat", padx=padding, pady=padding)
        card_frame.pack(padx=elevation, pady=elevation, fill=BOTH, expand=True)
        
        return card_frame, shadow_frame
    
    @staticmethod
    def create_modern_scrollable_frame(parent, width=None, height=None):
        """Crea un frame scrollable moderno con mejor funcionalidad"""
        # Frame contenedor principal
        container = tk.Frame(parent, bg=ModernColors.SURFACE)
        
        # Canvas para el scroll
        canvas = tk.Canvas(container, bg=ModernColors.SURFACE, 
                          highlightthickness=0, bd=0)
        if width:
            canvas.configure(width=width)
        if height:
            canvas.configure(height=height)
        
        # Scrollbar vertical moderna
        v_scrollbar = ttk.Scrollbar(container, orient="vertical", 
                                   command=canvas.yview)
        canvas.configure(yscrollcommand=v_scrollbar.set)
        
        # Frame interno scrollable
        scrollable_frame = tk.Frame(canvas, bg=ModernColors.SURFACE)
        scrollable_window = canvas.create_window((0, 0), window=scrollable_frame, 
                                               anchor="nw")
        
        def configure_scroll_region(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        
        def configure_canvas_width(event):
            canvas.itemconfig(scrollable_window, width=canvas.winfo_width())
        
        scrollable_frame.bind("<Configure>", configure_scroll_region)
        canvas.bind("<Configure>", configure_canvas_width)
        
        # Soporte para scroll con mouse wheel
        def on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        def bind_mousewheel(event):
            canvas.bind_all("<MouseWheel>", on_mousewheel)
        
        def unbind_mousewheel(event):
            canvas.unbind_all("<MouseWheel>")
        
        canvas.bind('<Enter>', bind_mousewheel)
        canvas.bind('<Leave>', unbind_mousewheel)
        
        # Pack elementos
        canvas.pack(side="left", fill="both", expand=True)
        v_scrollbar.pack(side="right", fill="y")
        
        return container, scrollable_frame, canvas
    
    @staticmethod
    def create_modern_frame(parent, bg_color=None):
        """Crea un marco moderno"""
        if bg_color is None:
            bg_color = ModernColors.SURFACE
        frame = tk.Frame(parent, bg=bg_color, bd=0, relief="flat")
        return frame
    
    @staticmethod
    def create_icon_button(parent, icon_text, text, command, bg_color=None, width=300):
        """Crea un botón con icono mejorado"""
        if bg_color is None:
            bg_color = ModernColors.PRIMARY
        
        return ModernStyleUtils.create_gradient_button(
            parent, text, command, icon_text, bg_color, bg_color, width, 55
        )
    
    @staticmethod
    def create_modern_label(parent, text, font_size=12, color=None, weight="normal", bg=None):
        """Crea una etiqueta moderna"""
        if color is None:
            color = ModernColors.TEXT_PRIMARY
        if bg is None:
            bg = ModernColors.SURFACE
        font = ("Segoe UI", font_size, weight)
        label = tk.Label(parent, text=text, font=font, fg=color, bg=bg, bd=0)
        return label

class DataManager:
    """Clase para manejar la persistencia de datos"""
    
    @staticmethod
    def load_events():
        """Carga eventos desde archivo JSON"""
        try:
            if os.path.exists("eventos.json"):
                with open("eventos.json", "r", encoding="utf-8") as file:
                    data = json.load(file)
                    return data.get("eventos", [])
        except Exception as e:
            print(f"Error al cargar eventos: {e}")
        return []
    
    @staticmethod
    def save_events(eventos):
        """Guarda eventos en archivo JSON"""
        try:
            data = {"eventos": eventos}
            with open("eventos.json", "w", encoding="utf-8") as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error al guardar eventos: {e}")
            return False
    
    @staticmethod
    def validate_event_data(fecha, tipo, nombre, hora_inicio, hora_fin):
        """Valida los datos del evento"""
        errors = []
        
        if not fecha.strip():
            errors.append("La fecha es requerida")
        
        if not tipo.strip():
            errors.append("El tipo de evento es requerido")
            
        if not nombre.strip():
            errors.append("El nombre del evento es requerido")
            
        try:
            inicio = datetime.strptime(hora_inicio, "%H:%M")
            fin = datetime.strptime(hora_fin, "%H:%M")
            if fin <= inicio:
                errors.append("La hora de fin debe ser posterior a la hora de inicio")
        except ValueError:
            errors.append("Formato de hora inválido")
        
        return errors

class NotificationManager:
    """Clase para manejar notificaciones y alertas"""
    
    @staticmethod
    def check_upcoming_events():
        """Verifica eventos próximos y devuelve notificaciones"""
        try:
            eventos = DataManager.load_events()
            notifications = []
            now = datetime.now()
            
            for evento in eventos:
                if isinstance(evento, dict):
                    fecha_str = evento.get("fecha", "")
                    hora_str = evento.get("hora_inicio", "")
                    nombre = evento.get("nombre", "")
                    tipo = evento.get("tipo", "")
                    
                    try:
                        # Convertir fecha y hora
                        fecha_evento = datetime.strptime(fecha_str, "%m/%d/%y")
                        hora_evento = datetime.strptime(hora_str, "%H:%M").time()
                        datetime_evento = datetime.combine(fecha_evento.date(), hora_evento)
                        
                        # Calcular diferencia de tiempo
                        diff = datetime_evento - now
                        
                        # Verificar si está dentro de las próximas 24 horas
                        if timedelta(0) <= diff <= timedelta(hours=24):
                            if diff <= timedelta(hours=1):
                                urgencia = "🔴 URGENTE"
                                color = ModernColors.ERROR
                            elif diff <= timedelta(hours=6):
                                urgencia = "🟡 PRÓXIMO"
                                color = ModernColors.WARNING
                            else:
                                urgencia = "🟢 HOY"
                                color = ModernColors.SUCCESS
                            
                            notifications.append({
                                "nombre": nombre,
                                "tipo": tipo,
                                "tiempo": diff,
                                "urgencia": urgencia,
                                "color": color,
                                "datetime": datetime_evento
                            })
                    except:
                        continue
            
            # Ordenar por proximidad
            notifications.sort(key=lambda x: x["tiempo"])
            return notifications
            
        except Exception as e:
            print(f"Error al verificar eventos próximos: {e}")
            return []

class AdvancedFeatures:
    """Clase para funcionalidades avanzadas"""
    
    @staticmethod
    def export_events_to_csv():
        """Exporta eventos a CSV"""
        try:
            eventos = DataManager.load_events()
            
            filename = f"agenda_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
            
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['fecha', 'tipo', 'nombre', 'hora_inicio', 'hora_fin', 'descripcion']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                for evento in eventos:
                    if isinstance(evento, dict):
                        writer.writerow({
                            'fecha': evento.get('fecha', ''),
                            'tipo': evento.get('tipo', ''),
                            'nombre': evento.get('nombre', ''),
                            'hora_inicio': evento.get('hora_inicio', ''),
                            'hora_fin': evento.get('hora_fin', ''),
                            'descripcion': evento.get('descripcion', '')
                        })
            
            return filename
        except Exception as e:
            print(f"Error al exportar: {e}")
            return None
    
    @staticmethod
    def get_time_statistics():
        """Calcula estadísticas de tiempo de eventos"""
        try:
            eventos = DataManager.load_events()
            stats = {
                "total_eventos": 0,
                "tiempo_total_horas": 0,
                "tipos_eventos": {},
                "eventos_por_mes": {},
                "promedio_duracion": 0
            }
            
            total_minutos = 0
            
            for evento in eventos:
                if isinstance(evento, dict):
                    stats["total_eventos"] += 1
                    
                    # Contar por tipo
                    tipo = evento.get("tipo", "Sin tipo")
                    stats["tipos_eventos"][tipo] = stats["tipos_eventos"].get(tipo, 0) + 1
                    
                    # Calcular duración
                    try:
                        inicio = datetime.strptime(evento.get("hora_inicio", "00:00"), "%H:%M")
                        fin = datetime.strptime(evento.get("hora_fin", "00:00"), "%H:%M")
                        duracion = (fin - inicio).seconds / 60  # en minutos
                        total_minutos += duracion
                    except:
                        pass
                    
                    # Contar por mes
                    try:
                        fecha = datetime.strptime(evento.get("fecha", ""), "%m/%d/%y")
                        mes_año = fecha.strftime("%Y-%m")
                        stats["eventos_por_mes"][mes_año] = stats["eventos_por_mes"].get(mes_año, 0) + 1
                    except:
                        pass
            
            stats["tiempo_total_horas"] = total_minutos / 60
            stats["promedio_duracion"] = total_minutos / stats["total_eventos"] if stats["total_eventos"] > 0 else 0
            
            return stats
        except Exception as e:
            print(f"Error al calcular estadísticas: {e}")
            return None
    
    @staticmethod
    def create_backup():
        """Crea un backup de todos los datos"""
        try:
            backup_data = {
                "created_at": datetime.now().isoformat(),
                "eventos": DataManager.load_events(),
                "version": "2.0"
            }
            
            filename = f"agenda_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(backup_data, f, indent=2, ensure_ascii=False)
            
            return filename
        except Exception as e:
            print(f"Error al crear backup: {e}")
            return None

class ModernMainWindow:
    def __init__(self, window):
        self.wind = window
        self.notifications = []
        self.setup_window()
        self.setup_styles()
        self.create_ui()
        self.update_clock()
        self.check_notifications()

    def setup_window(self):
        """Configura la ventana principal con mejor diseño"""
        self.wind.geometry("500x800")
        self.wind.configure(bg=ModernColors.BACKGROUND)
        self.wind.title('🗓️ Agenda Moderna Pro')
        self.wind.resizable(True, True)
        self.wind.minsize(450, 700)
        
        # Centrar ventana
        self.wind.update_idletasks()
        x = (self.wind.winfo_screenwidth() // 2) - (500 // 2)
        y = (self.wind.winfo_screenheight() // 2) - (800 // 2)
        self.wind.geometry(f"500x800+{x}+{y}")

    def setup_styles(self):
        """Configura estilos modernos"""
        ModernStyleUtils.configure_modern_style()
        
        # Fuentes personalizadas mejoradas
        self.font_title = tkFont.Font(family="Segoe UI", size=36, weight="bold")
        self.font_large = tkFont.Font(family="Segoe UI", size=24, weight="normal")
        self.font_medium = tkFont.Font(family="Segoe UI", size=16, weight="normal")
        self.font_small = tkFont.Font(family="Segoe UI", size=12, weight="normal")
        self.font_clock = tkFont.Font(family="Segoe UI", size=52, weight="normal")

    def create_ui(self):
        """Crea la interfaz de usuario mejorada"""
        # Container principal scrollable
        self.main_container, self.scrollable_frame, self.canvas = ModernStyleUtils.create_modern_scrollable_frame(
            self.wind, height=750)
        self.main_container.pack(fill=BOTH, expand=True, padx=15, pady=15)
        
        # Header mejorado con reloj y fecha
        self.create_header()
        
        # Panel de notificaciones
        self.create_notifications_panel()
        
        # Separador elegante
        self.create_separator()
        
        # Contenido principal
        self.create_main_content()
        
        # Panel de estadísticas rápidas
        self.create_stats_panel()

    def create_header(self):
        """Crea el header mejorado con reloj y fecha"""
        header_card, header_shadow = ModernStyleUtils.create_card_frame(self.scrollable_frame, padding=25, elevation=3)
        header_shadow.pack(fill=X, pady=(0, 20))
        
        # Reloj digital con mejor estilo
        clock_frame = ModernStyleUtils.create_modern_frame(header_card, ModernColors.CARD_BACKGROUND)
        clock_frame.pack(fill=X)
        
        self.clock_label = tk.Label(
            clock_frame,
            text="",
            font=self.font_clock,
            fg=ModernColors.PRIMARY_LIGHT,
            bg=ModernColors.CARD_BACKGROUND
        )
        self.clock_label.pack(pady=(0, 10))
        
        # Fecha y día con mejor formato
        self.date_label = tk.Label(
            clock_frame,
            text="",
            font=self.font_medium,
            fg=ModernColors.TEXT_SECONDARY,
            bg=ModernColors.CARD_BACKGROUND
        )
        self.date_label.pack()
        
        self.update_date()

    def create_notifications_panel(self):
        """Crea el panel de notificaciones"""
        self.notifications_frame = ModernStyleUtils.create_modern_frame(self.scrollable_frame)
        self.notifications_frame.pack(fill=X, pady=(0, 15))
        
        # Este frame se llenará dinámicamente con notificaciones

    def create_separator(self):
        """Crea un separador elegante"""
        separator_frame = ModernStyleUtils.create_modern_frame(self.scrollable_frame)
        separator_frame.pack(fill=X, pady=15)
        
        separator = tk.Frame(separator_frame, bg=ModernColors.DIVIDER_STRONG, height=2)
        separator.pack(fill=X, padx=50)

    def create_main_content(self):
        """Crea el contenido principal mejorado"""
        content_card, content_shadow = ModernStyleUtils.create_card_frame(self.scrollable_frame, padding=30)
        content_shadow.pack(fill=X, pady=(0, 20))
        
        # Título de la aplicación más elegante
        title_frame = ModernStyleUtils.create_modern_frame(content_card, ModernColors.CARD_BACKGROUND)
        title_frame.pack(fill=X, pady=(0, 20))
        
        title_label = tk.Label(
            title_frame,
            text="Mi Agenda Pro",
            font=self.font_title,
            fg=ModernColors.TEXT_PRIMARY,
            bg=ModernColors.CARD_BACKGROUND
        )
        title_label.pack()
        
        # Subtítulo con más información
        subtitle_label = tk.Label(
            title_frame,
            text="Organiza tu tiempo • Gestiona eventos • Alcanza tus metas",
            font=self.font_small,
            fg=ModernColors.TEXT_TERTIARY,
            bg=ModernColors.CARD_BACKGROUND
        )
        subtitle_label.pack(pady=(5, 0))
        
        # Botones principales mejorados
        self.create_main_buttons(content_card)

    def create_main_buttons(self, parent):
        """Crea los botones principales mejorados"""
        buttons_frame = ModernStyleUtils.create_modern_frame(parent, ModernColors.CARD_BACKGROUND)
        buttons_frame.pack(fill=X, pady=20)
        
        # Primera fila de botones
        row1 = ModernStyleUtils.create_modern_frame(buttons_frame, ModernColors.CARD_BACKGROUND)
        row1.pack(fill=X, pady=(0, 15))
        
        # Botón Calendario con gradiente
        calendar_btn = ModernStyleUtils.create_gradient_button(
            row1,
            "Gestionar Calendario",
            self.open_calendar,
            "📅",
            ModernColors.PRIMARY,
            ModernColors.PRIMARY_VARIANT,
            width=450,
            height=60
        )
        calendar_btn.pack(fill=X)
        
        # Segunda fila
        row2 = ModernStyleUtils.create_modern_frame(buttons_frame, ModernColors.CARD_BACKGROUND)
        row2.pack(fill=X, pady=(0, 15))
        
        # Botón Recordatorios
        reminder_btn = ModernStyleUtils.create_gradient_button(
            row2,
            "Ver Recordatorios",
            self.open_reminders,
            "🔔",
            ModernColors.SECONDARY,
            ModernColors.SECONDARY_VARIANT,
            width=450,
            height=60
        )
        reminder_btn.pack(fill=X)
        
        # Tercera fila - botones más pequeños
        row3 = ModernStyleUtils.create_modern_frame(buttons_frame, ModernColors.CARD_BACKGROUND)
        row3.pack(fill=X, pady=(0, 15))
        
        # Subframe para botones horizontales
        sub_buttons = ModernStyleUtils.create_modern_frame(row3, ModernColors.CARD_BACKGROUND)
        sub_buttons.pack(fill=X)
        
        # Botón Estadísticas
        stats_btn = ModernStyleUtils.create_gradient_button(
            sub_buttons,
            "Estadísticas",
            self.show_statistics,
            "📊",
            ModernColors.INFO,
            ModernColors.PRIMARY_VARIANT,
            width=210,
            height=50
        )
        stats_btn.pack(side=LEFT, padx=(0, 10))
        
        # Botón Configuración
        settings_btn = ModernStyleUtils.create_gradient_button(
            sub_buttons,
            "Configuración",
            self.open_settings,
            "⚙️",
            ModernColors.SURFACE_ELEVATED,
            ModernColors.SURFACE_VARIANT,
            width=210,
            height=50
        )
        settings_btn.pack(side=RIGHT)

    def create_stats_panel(self):
        """Crea el panel de estadísticas rápidas"""
        stats_card, stats_shadow = ModernStyleUtils.create_card_frame(self.scrollable_frame, padding=20)
        stats_shadow.pack(fill=X, pady=(0, 20))
        
        # Título del panel
        stats_title = tk.Label(
            stats_card,
            text="📈 Resumen Rápido",
            font=("Segoe UI", 16, "bold"),
            fg=ModernColors.TEXT_PRIMARY,
            bg=ModernColors.CARD_BACKGROUND
        )
        stats_title.pack(pady=(0, 15))
        
        # Frame para estadísticas
        self.stats_frame = ModernStyleUtils.create_modern_frame(stats_card, ModernColors.CARD_BACKGROUND)
        self.stats_frame.pack(fill=X)
        
        self.update_quick_stats()

    def update_quick_stats(self):
        """Actualiza las estadísticas rápidas"""
        try:
            # Limpiar frame anterior
            for widget in self.stats_frame.winfo_children():
                widget.destroy()
            
            # Obtener estadísticas
            stats = AdvancedFeatures.get_time_statistics()
            if stats:
                # Crear grid de estadísticas
                stats_grid = ModernStyleUtils.create_modern_frame(self.stats_frame, ModernColors.CARD_BACKGROUND)
                stats_grid.pack(fill=X)
                
                # Primera fila
                row1 = ModernStyleUtils.create_modern_frame(stats_grid, ModernColors.CARD_BACKGROUND)
                row1.pack(fill=X, pady=(0, 10))
                
                # Total eventos
                self.create_stat_item(row1, "📅", str(stats["total_eventos"]), "Eventos totales", LEFT)
                
                # Tiempo total
                hours = int(stats["tiempo_total_horas"])
                self.create_stat_item(row1, "⏰", f"{hours}h", "Tiempo total", RIGHT)
                
                # Segunda fila
                row2 = ModernStyleUtils.create_modern_frame(stats_grid, ModernColors.CARD_BACKGROUND)
                row2.pack(fill=X)
                
                # Duración promedio
                avg_mins = int(stats["promedio_duracion"])
                self.create_stat_item(row2, "📊", f"{avg_mins}min", "Duración promedio", LEFT)
                
                # Tipo más común
                if stats["tipos_eventos"]:
                    most_common = max(stats["tipos_eventos"], key=stats["tipos_eventos"].get)
                    self.create_stat_item(row2, "🏆", most_common, "Tipo favorito", RIGHT)
        except Exception as e:
            print(f"Error al actualizar estadísticas: {e}")

    def create_stat_item(self, parent, icon, value, label, side):
        """Crea un elemento de estadística"""
        item_frame = ModernStyleUtils.create_modern_frame(parent, ModernColors.CARD_BACKGROUND)
        item_frame.pack(side=side, padx=10)
        
        # Icono y valor
        value_frame = ModernStyleUtils.create_modern_frame(item_frame, ModernColors.CARD_BACKGROUND)
        value_frame.pack()
        
        icon_label = tk.Label(value_frame, text=icon, font=("Segoe UI", 16), 
                             fg=ModernColors.PRIMARY_LIGHT, bg=ModernColors.CARD_BACKGROUND)
        icon_label.pack(side=LEFT, padx=(0, 5))
        
        value_label = tk.Label(value_frame, text=value, font=("Segoe UI", 16, "bold"),
                              fg=ModernColors.TEXT_PRIMARY, bg=ModernColors.CARD_BACKGROUND)
        value_label.pack(side=LEFT)
        
        # Etiqueta
        label_label = tk.Label(item_frame, text=label, font=("Segoe UI", 10),
                              fg=ModernColors.TEXT_TERTIARY, bg=ModernColors.CARD_BACKGROUND)
        label_label.pack()

    def check_notifications(self):
        """Verifica y muestra notificaciones"""
        try:
            self.notifications = NotificationManager.check_upcoming_events()
            self.update_notifications_display()
            
            # Programar próxima verificación en 5 minutos
            self.wind.after(300000, self.check_notifications)
        except Exception as e:
            print(f"Error al verificar notificaciones: {e}")

    def update_notifications_display(self):
        """Actualiza la visualización de notificaciones"""
        # Limpiar notificaciones anteriores
        for widget in self.notifications_frame.winfo_children():
            widget.destroy()
        
        if self.notifications:
            # Crear header de notificaciones
            notif_header = tk.Label(
                self.notifications_frame,
                text="🔔 Eventos Próximos",
                font=("Segoe UI", 14, "bold"),
                fg=ModernColors.WARNING,
                bg=ModernColors.SURFACE
            )
            notif_header.pack(pady=(0, 10))
            
            # Mostrar hasta 3 notificaciones más urgentes
            for i, notif in enumerate(self.notifications[:3]):
                self.create_notification_item(notif)

    def create_notification_item(self, notification):
        """Crea un elemento de notificación"""
        notif_card, notif_shadow = ModernStyleUtils.create_card_frame(
            self.notifications_frame, padding=15, elevation=2)
        notif_shadow.pack(fill=X, pady=(0, 8))
        
        # Configurar color de fondo según urgencia
        notif_card.configure(bg=ModernColors.SURFACE_ELEVATED)
        
        # Frame principal de la notificación
        notif_content = ModernStyleUtils.create_modern_frame(notif_card, ModernColors.SURFACE_ELEVATED)
        notif_content.pack(fill=X)
        
        # Línea superior con urgencia y tiempo
        top_line = ModernStyleUtils.create_modern_frame(notif_content, ModernColors.SURFACE_ELEVATED)
        top_line.pack(fill=X, pady=(0, 5))
        
        urgencia_label = tk.Label(
            top_line,
            text=notification["urgencia"],
            font=("Segoe UI", 10, "bold"),
            fg=notification["color"],
            bg=ModernColors.SURFACE_ELEVATED
        )
        urgencia_label.pack(side=LEFT)
        
        # Tiempo restante
        tiempo = notification["tiempo"]
        if tiempo.days > 0:
            tiempo_str = f"en {tiempo.days} días"
        elif tiempo.seconds > 3600:
            horas = tiempo.seconds // 3600
            tiempo_str = f"en {horas}h"
        else:
            minutos = tiempo.seconds // 60
            tiempo_str = f"en {minutos}min"
        
        tiempo_label = tk.Label(
            top_line,
            text=tiempo_str,
            font=("Segoe UI", 10),
            fg=ModernColors.TEXT_TERTIARY,
            bg=ModernColors.SURFACE_ELEVATED
        )
        tiempo_label.pack(side=RIGHT)
        
        # Línea inferior con nombre y tipo
        bottom_line = ModernStyleUtils.create_modern_frame(notif_content, ModernColors.SURFACE_ELEVATED)
        bottom_line.pack(fill=X)
        
        nombre_label = tk.Label(
            bottom_line,
            text=notification["nombre"],
            font=("Segoe UI", 12, "bold"),
            fg=ModernColors.TEXT_PRIMARY,
            bg=ModernColors.SURFACE_ELEVATED
        )
        nombre_label.pack(side=LEFT)
        
        tipo_label = tk.Label(
            bottom_line,
            text=f"• {notification['tipo']}",
            font=("Segoe UI", 10),
            fg=ModernColors.TEXT_SECONDARY,
            bg=ModernColors.SURFACE_ELEVATED
        )
        tipo_label.pack(side=RIGHT)

    def update_clock(self):
        """Actualiza el reloj con efecto suave"""
        now = datetime.now()
        time_str = now.strftime("%H:%M:%S")
        self.clock_label.configure(text=time_str)
        self.wind.after(1000, self.update_clock)

    def update_date(self):
        """Actualiza la fecha con formato mejorado"""
        now = datetime.now()
        days = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                 "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        
        day_name = days[now.weekday()]
        month_name = months[now.month - 1]
        date_str = f"{day_name}, {now.day} de {month_name} de {now.year}"
        
        self.date_label.configure(text=date_str)

    def show_statistics(self):
        """Muestra la ventana de estadísticas detalladas"""
        self.wind.destroy()
        root = Tk()
        root.configure(bg=ModernColors.BACKGROUND)
        app = StatisticsWindow(root)
        root.mainloop()

    def open_calendar(self):
        """Abre la ventana del calendario"""
        self.wind.destroy()
        root = Tk()
        root.configure(bg=ModernColors.BACKGROUND)
        app = ModernCalendar(root)
        root.mainloop()

    def open_reminders(self):
        """Abre la ventana de recordatorios"""
        self.wind.destroy()
        root = Tk()
        root.configure(bg=ModernColors.BACKGROUND)
        app = ModernReminders(root)
        root.mainloop()

    def open_settings(self):
        """Abre la ventana de configuración"""
        self.wind.destroy()
        root = Tk()
        root.configure(bg=ModernColors.BACKGROUND)
        app = SettingsWindow(root)
        root.mainloop()

# Alias para mantener compatibilidad
index = ModernMainWindow

class StatisticsWindow:
    """Ventana de estadísticas detalladas"""
    
    def __init__(self, window):
        self.wind = window
        self.setup_window()
        self.create_ui()
    
    def setup_window(self):
        """Configura la ventana de estadísticas"""
        self.wind.geometry("800x600")
        self.wind.configure(bg=ModernColors.BACKGROUND)
        self.wind.title('📊 Estadísticas - Agenda Moderna')
        self.wind.resizable(True, True)
        
        # Centrar ventana
        self.wind.update_idletasks()
        x = (self.wind.winfo_screenwidth() // 2) - (800 // 2)
        y = (self.wind.winfo_screenheight() // 2) - (600 // 2)
        self.wind.geometry(f"800x600+{x}+{y}")
    
    def create_ui(self):
        """Crea la interfaz de estadísticas"""
        # Container principal scrollable
        main_container, scrollable_frame, canvas = ModernStyleUtils.create_modern_scrollable_frame(
            self.wind, height=550)
        main_container.pack(fill=BOTH, expand=True, padx=20, pady=20)
        
        # Header
        header_card, header_shadow = ModernStyleUtils.create_card_frame(scrollable_frame, padding=25)
        header_shadow.pack(fill=X, pady=(0, 20))
        
        title_label = tk.Label(
            header_card,
            text="📊 Estadísticas Detalladas",
            font=("Segoe UI", 24, "bold"),
            fg=ModernColors.TEXT_PRIMARY,
            bg=ModernColors.CARD_BACKGROUND
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            header_card,
            text="Análisis completo de tu productividad y gestión del tiempo",
            font=("Segoe UI", 12),
            fg=ModernColors.TEXT_SECONDARY,
            bg=ModernColors.CARD_BACKGROUND
        )
        subtitle_label.pack(pady=(5, 0))
        
        # Obtener y mostrar estadísticas
        stats = AdvancedFeatures.get_time_statistics()
        if stats:
            self.create_stats_display(scrollable_frame, stats)
        else:
            no_data_label = tk.Label(
                scrollable_frame,
                text="No hay datos suficientes para mostrar estadísticas",
                font=("Segoe UI", 14),
                fg=ModernColors.TEXT_TERTIARY,
                bg=ModernColors.SURFACE
            )
            no_data_label.pack(pady=50)
        
        # Botones de acción
        self.create_action_buttons(scrollable_frame)
    
    def create_stats_display(self, parent, stats):
        """Crea la visualización de estadísticas"""
        # Estadísticas generales
        general_card, general_shadow = ModernStyleUtils.create_card_frame(parent, padding=20)
        general_shadow.pack(fill=X, pady=(0, 15))
        
        general_title = tk.Label(
            general_card,
            text="📈 Resumen General",
            font=("Segoe UI", 16, "bold"),
            fg=ModernColors.PRIMARY,
            bg=ModernColors.CARD_BACKGROUND
        )
        general_title.pack(pady=(0, 15))
        
        # Grid de estadísticas generales
        general_grid = ModernStyleUtils.create_modern_frame(general_card, ModernColors.CARD_BACKGROUND)
        general_grid.pack(fill=X)
        
        # Primera fila
        row1 = ModernStyleUtils.create_modern_frame(general_grid, ModernColors.CARD_BACKGROUND)
        row1.pack(fill=X, pady=(0, 10))
        
        self.create_large_stat(row1, "📅", stats["total_eventos"], "Eventos Totales", LEFT)
        self.create_large_stat(row1, "⏰", f"{int(stats['tiempo_total_horas'])}h", "Tiempo Total", RIGHT)
        
        # Segunda fila
        row2 = ModernStyleUtils.create_modern_frame(general_grid, ModernColors.CARD_BACKGROUND)
        row2.pack(fill=X)
        
        self.create_large_stat(row2, "📊", f"{int(stats['promedio_duracion'])}min", "Duración Promedio", LEFT)
        self.create_large_stat(row2, "📆", len(stats["eventos_por_mes"]), "Meses Activos", RIGHT)
        
        # Tipos de eventos más populares
        if stats["tipos_eventos"]:
            types_card, types_shadow = ModernStyleUtils.create_card_frame(parent, padding=20)
            types_shadow.pack(fill=X, pady=(0, 15))
            
            types_title = tk.Label(
                types_card,
                text="🏆 Tipos de Eventos Más Populares",
                font=("Segoe UI", 16, "bold"),
                fg=ModernColors.SECONDARY,
                bg=ModernColors.CARD_BACKGROUND
            )
            types_title.pack(pady=(0, 15))
            
            # Mostrar top 5 tipos
            sorted_types = sorted(stats["tipos_eventos"].items(), key=lambda x: x[1], reverse=True)[:5]
            
            for i, (tipo, cantidad) in enumerate(sorted_types):
                type_frame = ModernStyleUtils.create_modern_frame(types_card, ModernColors.CARD_BACKGROUND)
                type_frame.pack(fill=X, pady=5)
                
                # Número de ranking
                rank_label = tk.Label(
                    type_frame,
                    text=f"{i+1}.",
                    font=("Segoe UI", 12, "bold"),
                    fg=ModernColors.PRIMARY,
                    bg=ModernColors.CARD_BACKGROUND,
                    width=3
                )
                rank_label.pack(side=LEFT)
                
                # Nombre del tipo
                type_label = tk.Label(
                    type_frame,
                    text=tipo,
                    font=("Segoe UI", 12),
                    fg=ModernColors.TEXT_PRIMARY,
                    bg=ModernColors.CARD_BACKGROUND
                )
                type_label.pack(side=LEFT, padx=(10, 0))
                
                # Cantidad
                count_label = tk.Label(
                    type_frame,
                    text=f"{cantidad} eventos",
                    font=("Segoe UI", 12, "bold"),
                    fg=ModernColors.ACCENT,
                    bg=ModernColors.CARD_BACKGROUND
                )
                count_label.pack(side=RIGHT)
        
        # Actividad por mes
        if stats["eventos_por_mes"]:
            months_card, months_shadow = ModernStyleUtils.create_card_frame(parent, padding=20)
            months_shadow.pack(fill=X, pady=(0, 15))
            
            months_title = tk.Label(
                months_card,
                text="📅 Actividad por Mes",
                font=("Segoe UI", 16, "bold"),
                fg=ModernColors.INFO,
                bg=ModernColors.CARD_BACKGROUND
            )
            months_title.pack(pady=(0, 15))
            
            # Mostrar últimos 6 meses
            sorted_months = sorted(stats["eventos_por_mes"].items())[-6:]
            
            for mes, cantidad in sorted_months:
                month_frame = ModernStyleUtils.create_modern_frame(months_card, ModernColors.CARD_BACKGROUND)
                month_frame.pack(fill=X, pady=3)
                
                # Formatear nombre del mes
                try:
                    fecha_mes = datetime.strptime(mes, "%Y-%m")
                    mes_nombre = fecha_mes.strftime("%B %Y")
                except:
                    mes_nombre = mes
                
                month_label = tk.Label(
                    month_frame,
                    text=mes_nombre,
                    font=("Segoe UI", 11),
                    fg=ModernColors.TEXT_PRIMARY,
                    bg=ModernColors.CARD_BACKGROUND
                )
                month_label.pack(side=LEFT)
                
                # Barra de progreso simple
                bar_frame = tk.Frame(month_frame, bg=ModernColors.SURFACE_VARIANT, height=8)
                bar_frame.pack(side=LEFT, fill=X, expand=True, padx=(10, 10), pady=4)
                
                # Calcular porcentaje (máximo = mayor cantidad de eventos en un mes)
                max_eventos = max(stats["eventos_por_mes"].values())
                porcentaje = (cantidad / max_eventos) * 100
                
                bar_fill = tk.Frame(bar_frame, bg=ModernColors.INFO, height=8)
                bar_fill.place(relwidth=porcentaje/100, relheight=1)
                
                count_label = tk.Label(
                    month_frame,
                    text=str(cantidad),
                    font=("Segoe UI", 11, "bold"),
                    fg=ModernColors.ACCENT,
                    bg=ModernColors.CARD_BACKGROUND
                )
                count_label.pack(side=RIGHT)
    
    def create_large_stat(self, parent, icon, value, label, side):
        """Crea una estadística grande"""
        stat_frame = ModernStyleUtils.create_modern_frame(parent, ModernColors.CARD_BACKGROUND)
        stat_frame.pack(side=side, expand=True, fill=X, padx=10)
        
        # Container central
        content_frame = ModernStyleUtils.create_modern_frame(stat_frame, ModernColors.CARD_BACKGROUND)
        content_frame.pack(expand=True)
        
        # Icono
        icon_label = tk.Label(
            content_frame,
            text=icon,
            font=("Segoe UI", 24),
            fg=ModernColors.PRIMARY_LIGHT,
            bg=ModernColors.CARD_BACKGROUND
        )
        icon_label.pack()
        
        # Valor
        value_label = tk.Label(
            content_frame,
            text=str(value),
            font=("Segoe UI", 20, "bold"),
            fg=ModernColors.TEXT_PRIMARY,
            bg=ModernColors.CARD_BACKGROUND
        )
        value_label.pack()
        
        # Etiqueta
        label_label = tk.Label(
            content_frame,
            text=label,
            font=("Segoe UI", 11),
            fg=ModernColors.TEXT_TERTIARY,
            bg=ModernColors.CARD_BACKGROUND
        )
        label_label.pack()
    
    def create_action_buttons(self, parent):
        """Crea los botones de acción"""
        buttons_card, buttons_shadow = ModernStyleUtils.create_card_frame(parent, padding=20)
        buttons_shadow.pack(fill=X, pady=(20, 0))
        
        buttons_frame = ModernStyleUtils.create_modern_frame(buttons_card, ModernColors.CARD_BACKGROUND)
        buttons_frame.pack(fill=X)
        
        # Botón exportar
        export_btn = ModernStyleUtils.create_gradient_button(
            buttons_frame,
            "Exportar Datos",
            self.export_data,
            "💾",
            ModernColors.SUCCESS,
            ModernColors.SECONDARY_VARIANT,
            width=350,
            height=50
        )
        export_btn.pack(pady=(0, 10))
        
        # Botón volver
        back_btn = ModernStyleUtils.create_gradient_button(
            buttons_frame,
            "Volver al Inicio",
            self.go_back,
            "⬅️",
            ModernColors.SURFACE_VARIANT,
            ModernColors.SURFACE_ELEVATED,
            width=350,
            height=50
        )
        back_btn.pack()
    
    def export_data(self):
        """Exporta los datos a CSV"""
        try:
            filename = AdvancedFeatures.export_events_to_csv()
            if filename:
                messagebox.showinfo("Éxito", f"Datos exportados a: {filename}")
            else:
                messagebox.showerror("Error", "No se pudieron exportar los datos")
        except Exception as e:
            messagebox.showerror("Error", f"Error al exportar: {str(e)}")
    
    def go_back(self):
        """Vuelve a la ventana principal"""
        self.wind.destroy()
        root = Tk()
        root.configure(bg=ModernColors.BACKGROUND)
        app = ModernMainWindow(root)
        root.mainloop()

class SettingsWindow:
    """Ventana de configuración"""
    
    def __init__(self, window):
        self.wind = window
        self.setup_window()
        self.create_ui()
    
    def setup_window(self):
        """Configura la ventana de configuración"""
        self.wind.geometry("600x700")
        self.wind.configure(bg=ModernColors.BACKGROUND)
        self.wind.title('⚙️ Configuración - Agenda Moderna')
        self.wind.resizable(True, True)
        
        # Centrar ventana
        self.wind.update_idletasks()
        x = (self.wind.winfo_screenwidth() // 2) - (600 // 2)
        y = (self.wind.winfo_screenheight() // 2) - (700 // 2)
        self.wind.geometry(f"600x700+{x}+{y}")
    
    def create_ui(self):
        """Crea la interfaz de configuración"""
        # Container principal scrollable
        main_container, scrollable_frame, canvas = ModernStyleUtils.create_modern_scrollable_frame(
            self.wind, height=650)
        main_container.pack(fill=BOTH, expand=True, padx=20, pady=20)
        
        # Header
        header_card, header_shadow = ModernStyleUtils.create_card_frame(scrollable_frame, padding=25)
        header_shadow.pack(fill=X, pady=(0, 20))
        
        title_label = tk.Label(
            header_card,
            text="⚙️ Configuración",
            font=("Segoe UI", 24, "bold"),
            fg=ModernColors.TEXT_PRIMARY,
            bg=ModernColors.CARD_BACKGROUND
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            header_card,
            text="Personaliza tu experiencia con la agenda",
            font=("Segoe UI", 12),
            fg=ModernColors.TEXT_SECONDARY,
            bg=ModernColors.CARD_BACKGROUND
        )
        subtitle_label.pack(pady=(5, 0))
        
        # Sección de respaldo
        self.create_backup_section(scrollable_frame)
        
        # Sección de notificaciones
        self.create_notifications_section(scrollable_frame)
        
        # Sección de datos
        self.create_data_section(scrollable_frame)
        
        # Botones de acción
        self.create_action_buttons(scrollable_frame)
    
    def create_backup_section(self, parent):
        """Crea la sección de respaldo"""
        backup_card, backup_shadow = ModernStyleUtils.create_card_frame(parent, padding=20)
        backup_shadow.pack(fill=X, pady=(0, 15))
        
        backup_title = tk.Label(
            backup_card,
            text="💾 Respaldo de Datos",
            font=("Segoe UI", 16, "bold"),
            fg=ModernColors.SUCCESS,
            bg=ModernColors.CARD_BACKGROUND
        )
        backup_title.pack(pady=(0, 15))
        
        backup_desc = tk.Label(
            backup_card,
            text="Mantén tus datos seguros creando copias de respaldo regulares",
            font=("Segoe UI", 11),
            fg=ModernColors.TEXT_SECONDARY,
            bg=ModernColors.CARD_BACKGROUND
        )
        backup_desc.pack(pady=(0, 15))
        
        # Botones de respaldo
        backup_buttons = ModernStyleUtils.create_modern_frame(backup_card, ModernColors.CARD_BACKGROUND)
        backup_buttons.pack(fill=X)
        
        # Crear backup JSON
        json_btn = ModernStyleUtils.create_gradient_button(
            backup_buttons,
            "Crear Backup JSON",
            self.create_json_backup,
            "📄",
            ModernColors.INFO,
            ModernColors.PRIMARY_VARIANT,
            width=250,
            height=45
        )
        json_btn.pack(side=LEFT, padx=(0, 10))
        
        # Crear backup CSV
        csv_btn = ModernStyleUtils.create_gradient_button(
            backup_buttons,
            "Exportar a CSV",
            self.create_csv_backup,
            "📊",
            ModernColors.SUCCESS,
            ModernColors.SECONDARY_VARIANT,
            width=250,
            height=45
        )
        csv_btn.pack(side=RIGHT)
    
    def create_notifications_section(self, parent):
        """Crea la sección de notificaciones"""
        notif_card, notif_shadow = ModernStyleUtils.create_card_frame(parent, padding=20)
        notif_shadow.pack(fill=X, pady=(0, 15))
        
        notif_title = tk.Label(
            notif_card,
            text="🔔 Notificaciones",
            font=("Segoe UI", 16, "bold"),
            fg=ModernColors.WARNING,
            bg=ModernColors.CARD_BACKGROUND
        )
        notif_title.pack(pady=(0, 15))
        
        notif_desc = tk.Label(
            notif_card,
            text="La aplicación verifica automáticamente eventos próximos cada 5 minutos",
            font=("Segoe UI", 11),
            fg=ModernColors.TEXT_SECONDARY,
            bg=ModernColors.CARD_BACKGROUND
        )
        notif_desc.pack(pady=(0, 10))
        
        # Info sobre notificaciones
        info_frame = ModernStyleUtils.create_modern_frame(notif_card, ModernColors.CARD_BACKGROUND)
        info_frame.pack(fill=X)
        
        info_items = [
            ("🔴 URGENTE", "Eventos en menos de 1 hora"),
            ("🟡 PRÓXIMO", "Eventos en las próximas 6 horas"),
            ("🟢 HOY", "Eventos programados para hoy")
        ]
        
        for icon, desc in info_items:
            item_frame = ModernStyleUtils.create_modern_frame(info_frame, ModernColors.CARD_BACKGROUND)
            item_frame.pack(fill=X, pady=2)
            
            icon_label = tk.Label(
                item_frame,
                text=icon,
                font=("Segoe UI", 10, "bold"),
                fg=ModernColors.TEXT_PRIMARY,
                bg=ModernColors.CARD_BACKGROUND
            )
            icon_label.pack(side=LEFT, padx=(0, 10))
            
            desc_label = tk.Label(
                item_frame,
                text=desc,
                font=("Segoe UI", 10),
                fg=ModernColors.TEXT_SECONDARY,
                bg=ModernColors.CARD_BACKGROUND
            )
            desc_label.pack(side=LEFT)
            item_frame = ModernStyleUtils.create_modern_frame(info_frame, ModernColors.CARD_BACKGROUND)
            item_frame.pack(fill=X, pady=2)
            
            icon_label = tk.Label(
                item_frame,
                text=icon,
                font=("Segoe UI", 10, "bold"),
                fg=ModernColors.TEXT_PRIMARY,
                bg=ModernColors.CARD_BACKGROUND
            )
            icon_label.pack(side=LEFT, padx=(0, 10))
            
            desc_label = tk.Label(
                item_frame,
                text=desc,
                font=("Segoe UI", 10),
                fg=ModernColors.TEXT_TERTIARY,
                bg=ModernColors.CARD_BACKGROUND
            )
            desc_label.pack(side=LEFT)
    
    def create_data_section(self, parent):
        """Crea la sección de gestión de datos"""
        data_card, data_shadow = ModernStyleUtils.create_card_frame(parent, padding=20)
        data_shadow.pack(fill=X, pady=(0, 15))
        
        data_title = tk.Label(
            data_card,
            text="🗂️ Gestión de Datos",
            font=("Segoe UI", 16, "bold"),
            fg=ModernColors.ERROR,
            bg=ModernColors.CARD_BACKGROUND
        )
        data_title.pack(pady=(0, 15))
        
        # Información de archivos
        files_info = ModernStyleUtils.create_modern_frame(data_card, ModernColors.CARD_BACKGROUND)
        files_info.pack(fill=X, pady=(0, 15))
        
        info_text = """Archivos de datos utilizados:
• eventos.json - Formato nuevo (recomendado)
• recordatorio.txt - Formato legacy (compatibilidad)

Los datos se guardan automáticamente en formato JSON para mejor rendimiento."""
        
        info_label = tk.Label(
            files_info,
            text=info_text,
            font=("Segoe UI", 10),
            fg=ModernColors.TEXT_SECONDARY,
            bg=ModernColors.CARD_BACKGROUND,
            justify=LEFT
        )
        info_label.pack(anchor=W)
        
        # Botón limpiar datos (con advertencia)
        warning_frame = ModernStyleUtils.create_modern_frame(data_card, ModernColors.CARD_BACKGROUND)
        warning_frame.pack(fill=X)
        
        warning_label = tk.Label(
            warning_frame,
            text="⚠️ Zona de peligro: Esta acción eliminará TODOS los eventos",
            font=("Segoe UI", 10, "bold"),
            fg=ModernColors.ERROR,
            bg=ModernColors.CARD_BACKGROUND
        )
        warning_label.pack(pady=(0, 10))
        
        clear_btn = tk.Button(
            warning_frame,
            text="🗑️ Eliminar Todos los Datos",
            command=self.clear_all_data,
            bg=ModernColors.ERROR,
            fg=ModernColors.TEXT_PRIMARY,
            font=("Segoe UI", 11, "bold"),
            bd=0,
            padx=20,
            pady=10,
            cursor="hand2"
        )
        clear_btn.pack()
    
    def create_action_buttons(self, parent):
        """Crea los botones de acción"""
        buttons_card, buttons_shadow = ModernStyleUtils.create_card_frame(parent, padding=20)
        buttons_shadow.pack(fill=X, pady=(20, 0))
        
        # Botón volver
        back_btn = ModernStyleUtils.create_gradient_button(
            buttons_card,
            "Volver al Inicio",
            self.go_back,
            "⬅️",
            ModernColors.SURFACE_VARIANT,
            ModernColors.SURFACE_ELEVATED,
            width=400,
            height=50
        )
        back_btn.pack()
    
    def create_json_backup(self):
        """Crea un backup en formato JSON"""
        try:
            filename = AdvancedFeatures.create_backup()
            if filename:
                messagebox.showinfo("Éxito", f"Backup creado: {filename}")
            else:
                messagebox.showerror("Error", "No se pudo crear el backup")
        except Exception as e:
            messagebox.showerror("Error", f"Error al crear backup: {str(e)}")
    
    def create_csv_backup(self):
        """Crea un backup en formato CSV"""
        try:
            filename = AdvancedFeatures.export_events_to_csv()
            if filename:
                messagebox.showinfo("Éxito", f"Datos exportados a: {filename}")
            else:
                messagebox.showerror("Error", "No se pudieron exportar los datos")
        except Exception as e:
            messagebox.showerror("Error", f"Error al exportar: {str(e)}")
    
    def clear_all_data(self):
        """Elimina todos los datos (con confirmación múltiple)"""
        # Primera confirmación
        if not messagebox.askyesno("⚠️ Confirmar", 
                                  "¿Estás seguro de que quieres eliminar TODOS los eventos?\n\nEsta acción NO se puede deshacer."):
            return
        
        # Segunda confirmación
        if not messagebox.askyesno("⚠️ Última confirmación", 
                                  "Esto eliminará permanentemente todos tus eventos.\n\n¿Estás COMPLETAMENTE seguro?"):
            return
        
        try:
            # Crear backup automático antes de eliminar
            backup_file = AdvancedFeatures.create_backup()
            
            # Eliminar archivo JSON
            if os.path.exists("eventos.json"):
                os.remove("eventos.json")
            
            # Eliminar archivo TXT legacy
            if os.path.exists("recordatorio.txt"):
                os.remove("recordatorio.txt")
            
            # Limpiar lista en memoria
            global lista
            lista = []
            
            backup_msg = f"\n\n📁 Backup automático creado: {backup_file}" if backup_file else ""
            messagebox.showinfo("✅ Completado", f"Todos los datos han sido eliminados.{backup_msg}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al eliminar datos: {str(e)}")
    
    def go_back(self):
        """Vuelve a la ventana principal"""
        self.wind.destroy()
        root = Tk()
        root.configure(bg=ModernColors.BACKGROUND)
        app = ModernMainWindow(root)
        root.mainloop()

class ModernCalendar:
    def __init__(self, window):
        self.wind = window
        self.setup_window()
        self.setup_variables()
        self.create_ui()
        self.load_events()

    def setup_window(self):
        """Configura la ventana del calendario mejorada"""
        self.wind.geometry("650x850")
        self.wind.configure(bg=ModernColors.BACKGROUND)
        self.wind.title('📅 Calendario - Agenda Moderna')
        self.wind.resizable(True, True)
        self.wind.minsize(600, 800)
        
        # Centrar ventana
        self.wind.update_idletasks()
        x = (self.wind.winfo_screenwidth() // 2) - (650 // 2)
        y = (self.wind.winfo_screenheight() // 2) - (850 // 2)
        self.wind.geometry(f"650x850+{x}+{y}")

    def setup_variables(self):
        """Configura las variables del formulario"""
        self.fecha_var = StringVar()
        self.tipo_var = StringVar()
        self.nombre_var = StringVar()
        self.hora_inicio_var = StringVar()
        self.hora_fin_var = StringVar()
        self.descripcion_var = StringVar()
        
        # Valores por defecto
        self.fecha_var.set(datetime.now().strftime("%m/%d/%y"))
        self.hora_inicio_var.set("09:00")
        self.hora_fin_var.set("10:00")

    def create_ui(self):
        """Crea la interfaz del calendario mejorada"""
        # Container principal scrollable
        main_container, scrollable_frame, canvas = ModernStyleUtils.create_modern_scrollable_frame(
            self.wind, height=800)
        main_container.pack(fill=BOTH, expand=True, padx=20, pady=20)
        
        self.scrollable_frame = scrollable_frame
        
        # Header mejorado
        self.create_header()
        
        # Vista previa del calendario
        self.create_calendar_preview()
        
        # Formulario mejorado
        self.create_form()
        
        # Botones de acción
        self.create_action_buttons()

    def create_header(self):
        """Crea el header del calendario mejorado"""
        header_card, header_shadow = ModernStyleUtils.create_card_frame(self.scrollable_frame, padding=25)
        header_shadow.pack(fill=X, pady=(0, 20))
        
        # Título con icono
        title_label = tk.Label(
            header_card,
            text="📅 Crear Nuevo Evento",
            font=("Segoe UI", 26, "bold"),
            fg=ModernColors.PRIMARY_LIGHT,
            bg=ModernColors.CARD_BACKGROUND
        )
        title_label.pack()
        
        # Subtítulo dinámico
        now = datetime.now()
        day_name = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"][now.weekday()]
        
        subtitle_label = tk.Label(
            header_card,
            text=f"Hoy es {day_name} • Planifica tu tiempo de manera inteligente",
            font=("Segoe UI", 12),
            fg=ModernColors.TEXT_SECONDARY,
            bg=ModernColors.CARD_BACKGROUND
        )
        subtitle_label.pack(pady=(5, 0))

    def create_calendar_preview(self):
        """Crea una vista previa del calendario"""
        preview_card, preview_shadow = ModernStyleUtils.create_card_frame(self.scrollable_frame, padding=20)
        preview_shadow.pack(fill=X, pady=(0, 20))
        
        preview_title = tk.Label(
            preview_card,
            text="🗓️ Seleccionar Fecha",
            font=("Segoe UI", 16, "bold"),
            fg=ModernColors.SECONDARY,
            bg=ModernColors.CARD_BACKGROUND
        )
        preview_title.pack(pady=(0, 15))
        
        try:
            # Calendar widget mejorado
            from tkcalendar import Calendar
            
            self.calendar_widget = Calendar(
                preview_card,
                selectmode='day',
                background=ModernColors.PRIMARY,
                foreground=ModernColors.TEXT_PRIMARY,
                bordercolor=ModernColors.BORDER,
                headersbackground=ModernColors.PRIMARY_VARIANT,
                headersforeground=ModernColors.TEXT_PRIMARY,
                selectbackground=ModernColors.ACCENT,
                selectforeground=ModernColors.TEXT_PRIMARY,
                normalbackground=ModernColors.SURFACE_VARIANT,
                normalforeground=ModernColors.TEXT_PRIMARY,
                weekendbackground=ModernColors.SURFACE_ELEVATED,
                weekendforeground=ModernColors.TEXT_SECONDARY,
                font=("Segoe UI", 10)
            )
            self.calendar_widget.pack(pady=(0, 15))
            
            # Sincronizar con variable de fecha
            def on_date_select(event=None):
                selected_date = self.calendar_widget.selection_get()
                self.fecha_var.set(selected_date.strftime("%m/%d/%y"))
            
            self.calendar_widget.bind("<<CalendarSelected>>", on_date_select)
            
        except Exception as e:
            print(f"Error al crear calendario: {e}")
            # Fallback a DateEntry si hay problemas con Calendar
            self.create_date_entry_fallback(preview_card)

    def create_date_entry_fallback(self, parent):
        """Crea un DateEntry como fallback"""
        date_frame = ModernStyleUtils.create_modern_frame(parent, ModernColors.CARD_BACKGROUND)
        date_frame.pack(fill=X)
        
        date_label = tk.Label(
            date_frame,
            text="Fecha del evento:",
            font=("Segoe UI", 12, "bold"),
            fg=ModernColors.TEXT_PRIMARY,
            bg=ModernColors.CARD_BACKGROUND
        )
        date_label.pack(pady=(0, 5))
        
        date_entry = DateEntry(
            date_frame,
            textvariable=self.fecha_var,
            width=12,
            background=ModernColors.PRIMARY,
            foreground=ModernColors.TEXT_PRIMARY,
            borderwidth=2,
            selectmode='day',
            font=("Segoe UI", 12)
        )
        date_entry.pack()

    def create_form(self):
        """Crea el formulario mejorado para eventos"""
        form_card, form_shadow = ModernStyleUtils.create_card_frame(self.scrollable_frame, padding=25)
        form_shadow.pack(fill=X, pady=(0, 20))
        
        form_title = tk.Label(
            form_card,
            text="📝 Detalles del Evento",
            font=("Segoe UI", 16, "bold"),
            fg=ModernColors.ACCENT,
            bg=ModernColors.CARD_BACKGROUND
        )
        form_title.pack(pady=(0, 20))
        
        # Grid de campos del formulario
        fields_frame = ModernStyleUtils.create_modern_frame(form_card, ModernColors.CARD_BACKGROUND)
        fields_frame.pack(fill=X)
        
        # Campo Tipo de evento
        self.create_enhanced_form_field(fields_frame, "🏷️ Tipo de evento", "tipo")
        
        # Campo Nombre
        self.create_enhanced_form_field(fields_frame, "📋 Nombre del evento", "nombre")
        
        # Frame para horarios
        time_frame = ModernStyleUtils.create_modern_frame(fields_frame, ModernColors.CARD_BACKGROUND)
        time_frame.pack(fill=X, pady=15)
        
        time_title = tk.Label(
            time_frame,
            text="⏰ Horario del Evento",
            font=("Segoe UI", 12, "bold"),
            fg=ModernColors.TEXT_PRIMARY,
            bg=ModernColors.CARD_BACKGROUND
        )
        time_title.pack(pady=(0, 10))
        
        # Horarios en una fila
        time_controls = ModernStyleUtils.create_modern_frame(time_frame, ModernColors.CARD_BACKGROUND)
        time_controls.pack(fill=X)
        
        # Hora inicio
        inicio_frame = ModernStyleUtils.create_modern_frame(time_controls, ModernColors.CARD_BACKGROUND)
        inicio_frame.pack(side=LEFT, expand=True, fill=X, padx=(0, 10))
        
        inicio_label = tk.Label(
            inicio_frame,
            text="Inicio:",
            font=("Segoe UI", 11, "bold"),
            fg=ModernColors.TEXT_SECONDARY,
            bg=ModernColors.CARD_BACKGROUND
        )
        inicio_label.pack(anchor=W)
        
        self.create_time_selector(inicio_frame, self.hora_inicio_var)
        
        # Hora fin
        fin_frame = ModernStyleUtils.create_modern_frame(time_controls, ModernColors.CARD_BACKGROUND)
        fin_frame.pack(side=RIGHT, expand=True, fill=X, padx=(10, 0))
        
        fin_label = tk.Label(
            fin_frame,
            text="Fin:",
            font=("Segoe UI", 11, "bold"),
            fg=ModernColors.TEXT_SECONDARY,
            bg=ModernColors.CARD_BACKGROUND
        )
        fin_label.pack(anchor=W)
        
        self.create_time_selector(fin_frame, self.hora_fin_var)
        
        # Campo Descripción
        self.create_enhanced_form_field(fields_frame, "📄 Descripción (opcional)", "descripcion", is_text=True)

    def create_enhanced_form_field(self, parent, label_text, field_type, is_text=False):
        """Crea un campo del formulario mejorado"""
        field_frame = ModernStyleUtils.create_modern_frame(parent, ModernColors.CARD_BACKGROUND)
        field_frame.pack(fill=X, pady=15)
        
        # Label con icono
        label = tk.Label(
            field_frame,
            text=label_text,
            font=("Segoe UI", 12, "bold"),
            fg=ModernColors.TEXT_PRIMARY,
            bg=ModernColors.CARD_BACKGROUND
        )
        label.pack(anchor=W, pady=(0, 8))
        
        # Campo específico según el tipo
        if field_type == "tipo":
            entry = ttk.Combobox(
                field_frame,
                textvariable=self.tipo_var,
                values=["Trabajo", "Estudio", "Personal", "Deporte", "Salud", 
                       "Reunión", "Cita", "Recordatorio", "Cumpleaños", "Viaje", 
                       "Compras", "Medicina", "Otro"],
                style="Modern.TCombobox",
                font=("Segoe UI", 12),
                state="readonly",
                height=8
            )
            entry.pack(fill=X, ipady=8)
            
        elif is_text:
            # Campo de texto multilinea para descripción
            text_frame = tk.Frame(field_frame, bg=ModernColors.SURFACE_VARIANT, bd=2)
            text_frame.pack(fill=X)
            
            text_widget = tk.Text(
                text_frame,
                height=4,
                font=("Segoe UI", 11),
                bg=ModernColors.SURFACE_VARIANT,
                fg=ModernColors.TEXT_PRIMARY,
                bd=0,
                padx=12,
                pady=8,
                wrap=tk.WORD,
                insertbackground=ModernColors.PRIMARY
            )
            text_widget.pack(fill=BOTH, expand=True)
            
            # Enlazar con variable
            def update_desc(*args):
                self.descripcion_var.set(text_widget.get("1.0", tk.END).strip())
            
            text_widget.bind("<KeyRelease>", update_desc)
            
        else:
            var = getattr(self, f"{field_type}_var")
            entry = ttk.Entry(
                field_frame,
                textvariable=var,
                style="Modern.TEntry",
                font=("Segoe UI", 12)
            )
            entry.pack(fill=X, ipady=8)

    def create_time_selector(self, parent, time_var):
        """Crea un selector de tiempo mejorado"""
        time_frame = ModernStyleUtils.create_modern_frame(parent, ModernColors.CARD_BACKGROUND)
        time_frame.pack(fill=X)
        
        # Combobox para horas
        hora_combo = ttk.Combobox(
            time_frame,
            values=[f"{i:02d}" for i in range(24)],
            width=4,
            style="Modern.TCombobox",
            state="readonly",
            font=("Segoe UI", 12)
        )
        hora_combo.pack(side=LEFT, padx=(0, 5))
        
        # Separador
        separator_label = tk.Label(
            time_frame, 
            text=":",
            font=("Segoe UI", 14, "bold"),
            fg=ModernColors.TEXT_PRIMARY,
            bg=ModernColors.CARD_BACKGROUND
        )
        separator_label.pack(side=LEFT, padx=2)
        
        # Combobox para minutos
        minutos_combo = ttk.Combobox(
            time_frame,
            values=[f"{i:02d}" for i in range(0, 60, 15)],
            width=4,
            style="Modern.TCombobox",
            state="readonly",
            font=("Segoe UI", 12)
        )
        minutos_combo.pack(side=LEFT, padx=(5, 0))
        
        # Inicializar valores
        current_time = time_var.get().split(":")
        if len(current_time) == 2:
            hora_combo.set(current_time[0])
            minutos_combo.set(current_time[1])
        
        # Función para actualizar la variable
        def update_time(*args):
            hora = hora_combo.get() or "00"
            minutos = minutos_combo.get() or "00"
            time_var.set(f"{hora}:{minutos}")
        
        hora_combo.bind('<<ComboboxSelected>>', update_time)
        minutos_combo.bind('<<ComboboxSelected>>', update_time)

    def create_action_buttons(self):
        """Crea los botones de acción mejorados"""
        buttons_card, buttons_shadow = ModernStyleUtils.create_card_frame(self.scrollable_frame, padding=25)
        buttons_shadow.pack(fill=X, pady=(0, 20))
        
        # Título de sección
        action_title = tk.Label(
            buttons_card,
            text="🎯 Acciones",
            font=("Segoe UI", 16, "bold"),
            fg=ModernColors.INFO,
            bg=ModernColors.CARD_BACKGROUND
        )
        action_title.pack(pady=(0, 20))
        
        # Primera fila de botones
        row1 = ModernStyleUtils.create_modern_frame(buttons_card, ModernColors.CARD_BACKGROUND)
        row1.pack(fill=X, pady=(0, 15))
        
        # Botón Guardar (principal)
        save_btn = ModernStyleUtils.create_gradient_button(
            row1,
            "Guardar Evento",
            self.save_event,
            "💾",
            ModernColors.SUCCESS,
            ModernColors.SECONDARY_VARIANT,
            width=600,
            height=55
        )
        save_btn.pack()
        
        # Segunda fila - botones secundarios
        row2 = ModernStyleUtils.create_modern_frame(buttons_card, ModernColors.CARD_BACKGROUND)
        row2.pack(fill=X, pady=(0, 15))
        
        # Botón Ver Eventos
        view_btn = ModernStyleUtils.create_gradient_button(
            row2,
            "Ver Todos los Eventos",
            self.view_events,
            "📋",
            ModernColors.INFO,
            ModernColors.PRIMARY_VARIANT,
            width=290,
            height=50
        )
        view_btn.pack(side=LEFT, padx=(0, 10))
        
        # Botón Limpiar Formulario
        clear_btn = ModernStyleUtils.create_gradient_button(
            row2,
            "Limpiar Formulario",
            self.clear_form,
            "🧹",
            ModernColors.WARNING,
            ModernColors.ACCENT_VARIANT,
            width=290,
            height=50
        )
        clear_btn.pack(side=RIGHT)
        
        # Tercera fila - navegación
        row3 = ModernStyleUtils.create_modern_frame(buttons_card, ModernColors.CARD_BACKGROUND)
        row3.pack(fill=X)
        
        # Botón Volver
        back_btn = ModernStyleUtils.create_gradient_button(
            row3,
            "Volver al Inicio",
            self.go_back,
            "⬅️",
            ModernColors.SURFACE_VARIANT,
            ModernColors.SURFACE_ELEVATED,
            width=600,
            height=50
        )
        back_btn.pack()

    def load_events(self):
        """Carga eventos existentes"""
        global lista
        lista = DataManager.load_events()

    def save_event(self):
        """Guarda un nuevo evento con validación mejorada"""
        try:
            # Validar datos
            errors = DataManager.validate_event_data(
                self.fecha_var.get(),
                self.tipo_var.get(),
                self.nombre_var.get(),
                self.hora_inicio_var.get(),
                self.hora_fin_var.get()
            )
            
            if errors:
                error_msg = "Por favor corrige los siguientes errores:\n\n"
                for i, error in enumerate(errors, 1):
                    error_msg += f"{i}. {error}\n"
                
                messagebox.showerror("❌ Error de validación", error_msg)
                return
            
            # Validaciones adicionales
            try:
                # Verificar que la fecha no sea en el pasado (opcional)
                fecha_evento = datetime.strptime(self.fecha_var.get(), "%m/%d/%y")
                if fecha_evento.date() < datetime.now().date():
                    if not messagebox.askyesno("📅 Fecha en el pasado", 
                                             "La fecha seleccionada ya pasó.\n¿Quieres continuar de todos modos?"):
                        return
                
                # Calcular duración del evento
                inicio = datetime.strptime(self.hora_inicio_var.get(), "%H:%M")
                fin = datetime.strptime(self.hora_fin_var.get(), "%H:%M")
                duracion_minutos = (fin - inicio).seconds // 60
                
            except Exception as e:
                messagebox.showerror("Error", f"Error al procesar fechas: {str(e)}")
                return
            
            # Crear evento
            evento = {
                "fecha": self.fecha_var.get(),
                "tipo": self.tipo_var.get(),
                "nombre": self.nombre_var.get(),
                "hora_inicio": self.hora_inicio_var.get(),
                "hora_fin": self.hora_fin_var.get(),
                "descripcion": self.descripcion_var.get(),
                "duracion_minutos": duracion_minutos,
                "created_at": datetime.now().isoformat(),
                "id": f"event_{int(datetime.now().timestamp())}"
            }
            
            # Agregar a la lista
            global lista
            lista.append(evento)
            
            # Guardar en archivo
            if DataManager.save_events(lista):
                # Mensaje de éxito con detalles
                success_msg = f"""✅ ¡Evento guardado exitosamente!

📅 Fecha: {self.fecha_var.get()}
🏷️ Tipo: {self.tipo_var.get()}
📋 Nombre: {self.nombre_var.get()}
⏰ Horario: {self.hora_inicio_var.get()} - {self.hora_fin_var.get()}
⏱️ Duración: {duracion_minutos} minutos"""
                
                messagebox.showinfo("Éxito", success_msg)
                self.clear_form()
            else:
                messagebox.showerror("❌ Error", "No se pudo guardar el evento")
                
        except Exception as e:
            messagebox.showerror("❌ Error inesperado", f"Ocurrió un error: {str(e)}")

    def clear_form(self):
        """Limpia el formulario con confirmación"""
        if self.nombre_var.get() or self.descripcion_var.get():
            if not messagebox.askyesno("🧹 Limpiar formulario", 
                                     "¿Estás seguro de que quieres limpiar el formulario?"):
                return
        
        # Limpiar todos los campos excepto la fecha actual
        self.fecha_var.set(datetime.now().strftime("%m/%d/%y"))
        self.tipo_var.set("")
        self.nombre_var.set("")
        self.hora_inicio_var.set("09:00")
        self.hora_fin_var.set("10:00")
        self.descripcion_var.set("")
        
        # Actualizar calendario si existe
        if hasattr(self, 'calendar_widget'):
            try:
                self.calendar_widget.selection_set(datetime.now().date())
            except:
                pass

    def view_events(self):
        """Abre la ventana de eventos"""
        self.wind.destroy()
        root = Tk()
        root.configure(bg=ModernColors.BACKGROUND)
        app = ModernReminders(root)
        root.mainloop()

    def go_back(self):
        """Vuelve a la ventana principal"""
        self.wind.destroy()
        root = Tk()
        root.configure(bg=ModernColors.BACKGROUND)
        app = ModernMainWindow(root)
        root.mainloop()

# Alias para compatibilidad
Calendario = ModernCalendar

class ModernReminders:
    def __init__(self, window):
        self.wind = window
        self.setup_window()
        self.search_var = StringVar()
        self.filter_var = StringVar()
        self.sort_var = StringVar()
        self.create_ui()
        self.load_and_display_events()

    def setup_window(self):
        """Configura la ventana de recordatorios mejorada"""
        self.wind.geometry("1100x750")
        self.wind.configure(bg=ModernColors.BACKGROUND)
        self.wind.title('🔔 Recordatorios - Agenda Moderna')
        self.wind.resizable(True, True)
        self.wind.minsize(900, 600)
        
        # Centrar ventana
        self.wind.update_idletasks()
        x = (self.wind.winfo_screenwidth() // 2) - (1100 // 2)
        y = (self.wind.winfo_screenheight() // 2) - (750 // 2)
        self.wind.geometry(f"1100x750+{x}+{y}")

    def create_ui(self):
        """Crea la interfaz de recordatorios mejorada"""
        # Container principal
        main_frame = ModernStyleUtils.create_modern_frame(self.wind)
        main_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)
        
        # Header mejorado
        self.create_header(main_frame)
        
        # Panel de controles (búsqueda, filtros, etc.)
        self.create_controls_panel(main_frame)
        
        # Lista de eventos mejorada
        self.create_events_list(main_frame)
        
        # Panel de información del evento seleccionado
        self.create_info_panel(main_frame)
        
        # Botones de acción
        self.create_action_buttons(main_frame)

    def create_header(self, parent):
        """Crea el header mejorado"""
        header_card, header_shadow = ModernStyleUtils.create_card_frame(parent, padding=25)
        header_shadow.pack(fill=X, pady=(0, 15))
        
        # Título principal
        title_label = tk.Label(
            header_card,
            text="🔔 Gestor de Recordatorios",
            font=("Segoe UI", 26, "bold"),
            fg=ModernColors.PRIMARY_LIGHT,
            bg=ModernColors.CARD_BACKGROUND
        )
        title_label.pack()
        
        # Subtítulo con información dinámica
        global lista
        total_eventos = len(lista) if lista else 0
        
        subtitle_label = tk.Label(
            header_card,
            text=f"Gestiona y organiza todos tus eventos • {total_eventos} eventos totales",
            font=("Segoe UI", 12),
            fg=ModernColors.TEXT_SECONDARY,
            bg=ModernColors.CARD_BACKGROUND
        )
        subtitle_label.pack(pady=(5, 0))

    def create_controls_panel(self, parent):
        """Crea el panel de controles mejorado"""
        controls_card, controls_shadow = ModernStyleUtils.create_card_frame(parent, padding=20)
        controls_shadow.pack(fill=X, pady=(0, 15))
        
        # Título del panel
        controls_title = tk.Label(
            controls_card,
            text="🔍 Buscar y Filtrar",
            font=("Segoe UI", 16, "bold"),
            fg=ModernColors.SECONDARY,
            bg=ModernColors.CARD_BACKGROUND
        )
        controls_title.pack(pady=(0, 15))
        
        # Frame para controles en una fila
        controls_row = ModernStyleUtils.create_modern_frame(controls_card, ModernColors.CARD_BACKGROUND)
        controls_row.pack(fill=X)
        
        # Búsqueda
        search_frame = ModernStyleUtils.create_modern_frame(controls_row, ModernColors.CARD_BACKGROUND)
        search_frame.pack(side=LEFT, expand=True, fill=X, padx=(0, 10))
        
        search_label = tk.Label(
            search_frame,
            text="🔍 Buscar:",
            font=("Segoe UI", 11, "bold"),
            fg=ModernColors.TEXT_PRIMARY,
            bg=ModernColors.CARD_BACKGROUND
        )
        search_label.pack(anchor=W, pady=(0, 5))
        
        search_entry = ttk.Entry(
            search_frame,
            textvariable=self.search_var,
            style="Modern.TEntry",
            font=("Segoe UI", 11)
        )
        search_entry.pack(fill=X, ipady=6)
        search_entry.bind('<KeyRelease>', self.filter_events)
        
        # Filtro por tipo
        filter_frame = ModernStyleUtils.create_modern_frame(controls_row, ModernColors.CARD_BACKGROUND)
        filter_frame.pack(side=LEFT, padx=10)
        
        filter_label = tk.Label(
            filter_frame,
            text="🏷️ Filtrar por tipo:",
            font=("Segoe UI", 11, "bold"),
            fg=ModernColors.TEXT_PRIMARY,
            bg=ModernColors.CARD_BACKGROUND
        )
        filter_label.pack(anchor=W, pady=(0, 5))
        
        filter_combo = ttk.Combobox(
            filter_frame,
            textvariable=self.filter_var,
            values=["Todos", "Trabajo", "Estudio", "Personal", "Deporte", "Salud", 
                   "Reunión", "Cita", "Recordatorio", "Cumpleaños", "Otro"],
            style="Modern.TCombobox",
            font=("Segoe UI", 11),
            state="readonly",
            width=12
        )
        filter_combo.pack(ipady=6)
        filter_combo.set("Todos")
        filter_combo.bind('<<ComboboxSelected>>', self.filter_events)
        
        # Ordenar
        sort_frame = ModernStyleUtils.create_modern_frame(controls_row, ModernColors.CARD_BACKGROUND)
        sort_frame.pack(side=RIGHT, padx=(10, 0))
        
        sort_label = tk.Label(
            sort_frame,
            text="📊 Ordenar por:",
            font=("Segoe UI", 11, "bold"),
            fg=ModernColors.TEXT_PRIMARY,
            bg=ModernColors.CARD_BACKGROUND
        )
        sort_label.pack(anchor=W, pady=(0, 5))
        
        sort_combo = ttk.Combobox(
            sort_frame,
            textvariable=self.sort_var,
            values=["Fecha (próximos)", "Fecha (antiguos)", "Nombre A-Z", "Nombre Z-A", "Tipo"],
            style="Modern.TCombobox",
            font=("Segoe UI", 11),
            state="readonly",
            width=15
        )
        sort_combo.pack(ipady=6)
        sort_combo.set("Fecha (próximos)")
        sort_combo.bind('<<ComboboxSelected>>', self.filter_events)

    def create_events_list(self, parent):
        """Crea la lista de eventos mejorada"""
        # Frame contenedor
        list_card, list_shadow = ModernStyleUtils.create_card_frame(parent, padding=20)
        list_shadow.pack(fill=BOTH, expand=True, pady=(0, 15))
        
        # Título de la lista
        list_title = tk.Label(
            list_card,
            text="📋 Lista de Eventos",
            font=("Segoe UI", 16, "bold"),
            fg=ModernColors.ACCENT,
            bg=ModernColors.CARD_BACKGROUND
        )
        list_title.pack(pady=(0, 15))
        
        # Container para el Treeview y scrollbars
        tree_container = ModernStyleUtils.create_modern_frame(list_card, ModernColors.CARD_BACKGROUND)
        tree_container.pack(fill=BOTH, expand=True)
        
        # Crear Treeview con columnas mejoradas
        columns = ("Fecha", "Tipo", "Nombre", "Horario", "Duración", "Estado")
        self.events_tree = ttk.Treeview(
            tree_container, 
            columns=columns, 
            show='headings', 
            height=15,
            style="Modern.Treeview"
        )
        
        # Configurar columnas con mejor distribución
        column_widths = {
            "Fecha": 100,
            "Tipo": 100,
            "Nombre": 250,
            "Horario": 120,
            "Duración": 80,
            "Estado": 100
        }
        
        for col in columns:
            self.events_tree.heading(col, text=col, command=lambda c=col: self.sort_by_column(c))
            self.events_tree.column(col, width=column_widths[col], minwidth=50)
        
        # Scrollbars
        v_scrollbar = ttk.Scrollbar(tree_container, orient=VERTICAL, command=self.events_tree.yview)
        h_scrollbar = ttk.Scrollbar(tree_container, orient=HORIZONTAL, command=self.events_tree.xview)
        
        self.events_tree.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        
        # Grid layout para scrollbars
        self.events_tree.grid(row=0, column=0, sticky="nsew")
        v_scrollbar.grid(row=0, column=1, sticky="ns")
        h_scrollbar.grid(row=1, column=0, sticky="ew")
        
        tree_container.grid_rowconfigure(0, weight=1)
        tree_container.grid_columnconfigure(0, weight=1)
        
        # Bind eventos
        self.events_tree.bind('<<TreeviewSelect>>', self.on_event_select)
        self.events_tree.bind('<Double-1>', self.on_event_double_click)

    def create_info_panel(self, parent):
        """Crea el panel de información del evento seleccionado"""
        self.info_card, info_shadow = ModernStyleUtils.create_card_frame(parent, padding=20)
        info_shadow.pack(fill=X, pady=(0, 15))
        
        # Título del panel
        info_title = tk.Label(
            self.info_card,
            text="ℹ️ Información del Evento",
            font=("Segoe UI", 16, "bold"),
            fg=ModernColors.INFO,
            bg=ModernColors.CARD_BACKGROUND
        )
        info_title.pack(pady=(0, 15))
        
        # Contenido del panel (se actualiza dinámicamente)
        self.info_content = ModernStyleUtils.create_modern_frame(self.info_card, ModernColors.CARD_BACKGROUND)
        self.info_content.pack(fill=X)
        
        # Mensaje inicial
        self.show_info_message("Selecciona un evento para ver sus detalles")

    def show_info_message(self, message):
        """Muestra un mensaje en el panel de información"""
        # Limpiar contenido anterior
        for widget in self.info_content.winfo_children():
            widget.destroy()
        
        message_label = tk.Label(
            self.info_content,
            text=message,
            font=("Segoe UI", 12),
            fg=ModernColors.TEXT_TERTIARY,
            bg=ModernColors.CARD_BACKGROUND
        )
        message_label.pack(pady=20)

    def show_event_details(self, event_data):
        """Muestra los detalles de un evento seleccionado"""
        # Limpiar contenido anterior
        for widget in self.info_content.winfo_children():
            widget.destroy()
        
        if isinstance(event_data, dict):
            # Grid de información
            details_grid = ModernStyleUtils.create_modern_frame(self.info_content, ModernColors.CARD_BACKGROUND)
            details_grid.pack(fill=X)
            
            # Primera fila
            row1 = ModernStyleUtils.create_modern_frame(details_grid, ModernColors.CARD_BACKGROUND)
            row1.pack(fill=X, pady=(0, 10))
            
            self.create_detail_item(row1, "📅", "Fecha:", event_data.get("fecha", "N/A"), LEFT)
            self.create_detail_item(row1, "🏷️", "Tipo:", event_data.get("tipo", "N/A"), RIGHT)
            
            # Segunda fila
            row2 = ModernStyleUtils.create_modern_frame(details_grid, ModernColors.CARD_BACKGROUND)
            row2.pack(fill=X, pady=(0, 10))
            
            self.create_detail_item(row2, "📋", "Nombre:", event_data.get("nombre", "N/A"), LEFT)
            
            # Tercera fila
            row3 = ModernStyleUtils.create_modern_frame(details_grid, ModernColors.CARD_BACKGROUND)
            row3.pack(fill=X, pady=(0, 10))
            
            horario = f"{event_data.get('hora_inicio', 'N/A')} - {event_data.get('hora_fin', 'N/A')}"
            self.create_detail_item(row3, "⏰", "Horario:", horario, LEFT)
            
            duracion = event_data.get("duracion_minutos", 0)
            duracion_str = f"{duracion} min" if duracion else "N/A"
            self.create_detail_item(row3, "⏱️", "Duración:", duracion_str, RIGHT)
            
            # Descripción (si existe)
            descripcion = event_data.get("descripcion", "").strip()
            if descripcion:
                desc_frame = ModernStyleUtils.create_modern_frame(details_grid, ModernColors.CARD_BACKGROUND)
                desc_frame.pack(fill=X, pady=(10, 0))
                
                desc_label = tk.Label(
                    desc_frame,
                    text="📄 Descripción:",
                    font=("Segoe UI", 11, "bold"),
                    fg=ModernColors.TEXT_PRIMARY,
                    bg=ModernColors.CARD_BACKGROUND
                )
                desc_label.pack(anchor=W, pady=(0, 5))
                
                desc_text = tk.Label(
                    desc_frame,
                    text=descripcion,
                    font=("Segoe UI", 11),
                    fg=ModernColors.TEXT_SECONDARY,
                    bg=ModernColors.CARD_BACKGROUND,
                    wraplength=400,
                    justify=LEFT
                )
                desc_text.pack(anchor=W, padx=(20, 0))

    def create_detail_item(self, parent, icon, label, value, side):
        """Crea un elemento de detalle"""
        item_frame = ModernStyleUtils.create_modern_frame(parent, ModernColors.CARD_BACKGROUND)
        item_frame.pack(side=side, expand=True, fill=X, padx=10)
        
        # Línea superior con icono y etiqueta
        header_frame = ModernStyleUtils.create_modern_frame(item_frame, ModernColors.CARD_BACKGROUND)
        header_frame.pack(fill=X)
        
        icon_label = tk.Label(
            header_frame,
            text=icon,
            font=("Segoe UI", 12),
            fg=ModernColors.PRIMARY_LIGHT,
            bg=ModernColors.CARD_BACKGROUND
        )
        icon_label.pack(side=LEFT, padx=(0, 5))
        
        label_label = tk.Label(
            header_frame,
            text=label,
            font=("Segoe UI", 11, "bold"),
            fg=ModernColors.TEXT_PRIMARY,
            bg=ModernColors.CARD_BACKGROUND
        )
        label_label.pack(side=LEFT)
        
        # Valor
        value_label = tk.Label(
            item_frame,
            text=value,
            font=("Segoe UI", 11),
            fg=ModernColors.TEXT_SECONDARY,
            bg=ModernColors.CARD_BACKGROUND
        )
        value_label.pack(anchor=W, padx=(17, 0))

    def create_action_buttons(self, parent):
        """Crea los botones de acción mejorados"""
        buttons_card, buttons_shadow = ModernStyleUtils.create_card_frame(parent, padding=20)
        buttons_shadow.pack(fill=X)
        
        # Título de acciones
        actions_title = tk.Label(
            buttons_card,
            text="🎯 Acciones",
            font=("Segoe UI", 16, "bold"),
            fg=ModernColors.WARNING,
            bg=ModernColors.CARD_BACKGROUND
        )
        actions_title.pack(pady=(0, 15))
        
        # Primera fila de botones
        row1 = ModernStyleUtils.create_modern_frame(buttons_card, ModernColors.CARD_BACKGROUND)
        row1.pack(fill=X, pady=(0, 10))
        
        # Botón nuevo evento
        new_btn = ModernStyleUtils.create_gradient_button(
            row1,
            "Nuevo Evento",
            self.new_event,
            "➕",
            ModernColors.SUCCESS,
            ModernColors.SECONDARY_VARIANT,
            width=250,
            height=50
        )
        new_btn.pack(side=LEFT, padx=(0, 10))
        
        # Botón eliminar seleccionado
        delete_btn = ModernStyleUtils.create_gradient_button(
            row1,
            "Eliminar Seleccionado",
            self.delete_selected_event,
            "🗑️",
            ModernColors.ERROR,
            ModernColors.WARNING,
            width=250,
            height=50
        )
        delete_btn.pack(side=LEFT, padx=5)
        
        # Botón exportar
        export_btn = ModernStyleUtils.create_gradient_button(
            row1,
            "Exportar Datos",
            self.export_events,
            "💾",
            ModernColors.INFO,
            ModernColors.PRIMARY_VARIANT,
            width=250,
            height=50
        )
        export_btn.pack(side=RIGHT, padx=(10, 0))
        
        # Segunda fila - navegación
        row2 = ModernStyleUtils.create_modern_frame(buttons_card, ModernColors.CARD_BACKGROUND)
        row2.pack(fill=X)
        
        # Botón volver
        back_btn = ModernStyleUtils.create_gradient_button(
            row2,
            "Volver al Inicio",
            self.go_back,
            "⬅️",
            ModernColors.SURFACE_VARIANT,
            ModernColors.SURFACE_ELEVATED,
            width=780,
            height=50
        )
        back_btn.pack()

    def load_and_display_events(self):
        """Carga y muestra los eventos"""
        global lista
        lista = DataManager.load_events()
        self.display_events(lista)

    def display_events(self, events):
        """Muestra los eventos en la lista mejorada"""
        # Limpiar lista
        for item in self.events_tree.get_children():
            self.events_tree.delete(item)
        
        if not events:
            self.show_info_message("No hay eventos para mostrar")
            return
        
        # Agregar eventos
        for i, event in enumerate(events):
            if isinstance(event, dict):
                # Formato nuevo (JSON)
                fecha = event.get("fecha", "")
                tipo = event.get("tipo", "")
                nombre = event.get("nombre", "")
                hora_inicio = event.get("hora_inicio", "")
                hora_fin = event.get("hora_fin", "")
                horario = f"{hora_inicio} - {hora_fin}"
                
                # Calcular duración
                duracion = event.get("duracion_minutos", 0)
                duracion_str = f"{duracion}min" if duracion else "N/A"
                
                # Determinar estado basado en fecha y hora
                estado = self.get_event_status(fecha, hora_inicio)
                
                # Colores según estado
                if estado == "Pasado":
                    tag = "pasado"
                elif estado == "Hoy":
                    tag = "hoy"
                elif estado == "Mañana":
                    tag = "mañana"
                else:
                    tag = "futuro"
                
            else:
                # Formato antiguo (string con $)
                parts = str(event).split("$")
                if len(parts) >= 7:
                    fecha = parts[0]
                    tipo = parts[1]
                    nombre = parts[2]
                    hora_inicio = f"{parts[3]}:{parts[4]}"
                    hora_fin = f"{parts[5]}:{parts[6]}"
                    horario = f"{hora_inicio} - {hora_fin}"
                    
                    # Calcular duración aproximada
                    try:
                        inicio = datetime.strptime(hora_inicio, "%H:%M")
                        fin = datetime.strptime(hora_fin, "%H:%M")
                        duracion_mins = (fin - inicio).seconds // 60
                        duracion_str = f"{duracion_mins}min"
                    except:
                        duracion_str = "N/A"
                    
                    estado = self.get_event_status(fecha, hora_inicio)
                    tag = "legacy"
                else:
                    continue
            
            # Insertar en la lista con tag para colores
            item_id = self.events_tree.insert("", "end", values=(fecha, tipo, nombre, horario, duracion_str, estado), tags=(tag,))
        
        # Configurar colores de tags
        self.events_tree.tag_configure("pasado", foreground=ModernColors.TEXT_MUTED)
        self.events_tree.tag_configure("hoy", foreground=ModernColors.SUCCESS, font=("Segoe UI", 11, "bold"))
        self.events_tree.tag_configure("mañana", foreground=ModernColors.WARNING, font=("Segoe UI", 11, "bold"))
        self.events_tree.tag_configure("futuro", foreground=ModernColors.INFO)
        self.events_tree.tag_configure("legacy", foreground=ModernColors.TEXT_TERTIARY)

    def get_event_status(self, fecha_str, hora_str):
        """Determina el estado del evento"""
        try:
            # Convertir fecha y hora a datetime
            fecha_evento = datetime.strptime(fecha_str, "%m/%d/%y")
            hora_evento = datetime.strptime(hora_str, "%H:%M").time()
            datetime_evento = datetime.combine(fecha_evento.date(), hora_evento)
            
            now = datetime.now()
            
            if datetime_evento < now:
                return "Pasado"
            elif datetime_evento.date() == now.date():
                return "Hoy"
            elif datetime_evento.date() == (now + timedelta(days=1)).date():
                return "Mañana"
            else:
                return "Futuro"
        except:
            return "Sin fecha"

    def filter_events(self, event=None):
        """Filtra y ordena eventos"""
        search_text = self.search_var.get().lower()
        filter_type = self.filter_var.get()
        sort_by = self.sort_var.get()
        
        global lista
        
        # Aplicar filtros
        filtered_events = []
        for event in lista:
            # Filtro por búsqueda
            if search_text:
                if isinstance(event, dict):
                    searchable_text = f"{event.get('nombre', '')} {event.get('tipo', '')} {event.get('descripcion', '')}".lower()
                else:
                    searchable_text = str(event).lower()
                
                if search_text not in searchable_text:
                    continue
            
            # Filtro por tipo
            if filter_type != "Todos":
                if isinstance(event, dict):
                    if event.get("tipo", "") != filter_type:
                        continue
                else:
                    parts = str(event).split("$")
                    if len(parts) > 1 and parts[1] != filter_type:
                        continue
            
            filtered_events.append(event)
        
        # Aplicar ordenamiento
        if sort_by == "Fecha (próximos)":
            filtered_events.sort(key=lambda x: self.get_sort_date(x))
        elif sort_by == "Fecha (antiguos)":
            filtered_events.sort(key=lambda x: self.get_sort_date(x), reverse=True)
        elif sort_by == "Nombre A-Z":
            filtered_events.sort(key=lambda x: self.get_sort_name(x))
        elif sort_by == "Nombre Z-A":
            filtered_events.sort(key=lambda x: self.get_sort_name(x), reverse=True)
        elif sort_by == "Tipo":
            filtered_events.sort(key=lambda x: self.get_sort_type(x))
        
        self.display_events(filtered_events)

    def get_sort_date(self, event):
        """Obtiene fecha para ordenamiento"""
        try:
            if isinstance(event, dict):
                fecha_str = event.get("fecha", "")
            else:
                parts = str(event).split("$")
                fecha_str = parts[0] if parts else ""
            
            return datetime.strptime(fecha_str, "%m/%d/%y")
        except:
            return datetime.min

    def get_sort_name(self, event):
        """Obtiene nombre para ordenamiento"""
        if isinstance(event, dict):
            return event.get("nombre", "").lower()
        else:
            parts = str(event).split("$")
            return parts[2].lower() if len(parts) > 2 else ""

    def get_sort_type(self, event):
        """Obtiene tipo para ordenamiento"""
        if isinstance(event, dict):
            return event.get("tipo", "").lower()
        else:
            parts = str(event).split("$")
            return parts[1].lower() if len(parts) > 1 else ""

    def sort_by_column(self, column):
        """Ordena por columna específica"""
        if column == "Fecha":
            self.sort_var.set("Fecha (próximos)")
        elif column == "Nombre":
            current = self.sort_var.get()
            if current == "Nombre A-Z":
                self.sort_var.set("Nombre Z-A")
            else:
                self.sort_var.set("Nombre A-Z")
        elif column == "Tipo":
            self.sort_var.set("Tipo")
        
        self.filter_events()

    def on_event_select(self, event=None):
        """Maneja la selección de eventos"""
        selection = self.events_tree.selection()
        if not selection:
            self.show_info_message("Selecciona un evento para ver sus detalles")
            return
        
        # Obtener datos del evento seleccionado
        item = selection[0]
        values = self.events_tree.item(item, 'values')
        
        if values:
            # Buscar el evento completo en la lista
            global lista
            for event in lista:
                if isinstance(event, dict):
                    if (event.get("nombre", "") == values[2] and 
                        event.get("fecha", "") == values[0]):
                        self.show_event_details(event)
                        break
                else:
                    parts = str(event).split("$")
                    if len(parts) > 2 and parts[2] == values[2] and parts[0] == values[0]:
                        # Convertir evento legacy a formato dict para mostrar
                        legacy_event = {
                            "fecha": parts[0] if len(parts) > 0 else "",
                            "tipo": parts[1] if len(parts) > 1 else "",
                            "nombre": parts[2] if len(parts) > 2 else "",
                            "hora_inicio": f"{parts[3]}:{parts[4]}" if len(parts) > 4 else "",
                            "hora_fin": f"{parts[5]}:{parts[6]}" if len(parts) > 6 else "",
                            "descripcion": "Evento en formato legacy"
                        }
                        self.show_event_details(legacy_event)
                        break

    def on_event_double_click(self, event=None):
        """Maneja doble clic en eventos"""
        # Por ahora, solo muestra información
        messagebox.showinfo("Función futura", "La edición de eventos se implementará próximamente")

    def delete_selected_event(self):
        """Elimina el evento seleccionado con confirmación mejorada"""
        selection = self.events_tree.selection()
        if not selection:
            messagebox.showwarning("⚠️ Selección requerida", 
                                 "Por favor selecciona un evento para eliminar")
            return
        
        # Obtener información del evento
        item = selection[0]
        values = self.events_tree.item(item, 'values')
        evento_nombre = values[2] if len(values) > 2 else "Evento sin nombre"
        
        # Confirmar eliminación con más detalles
        confirm_msg = f"""¿Estás seguro de que quieres eliminar este evento?

📋 Nombre: {evento_nombre}
📅 Fecha: {values[0] if len(values) > 0 else 'N/A'}
🏷️ Tipo: {values[1] if len(values) > 1 else 'N/A'}

⚠️ Esta acción no se puede deshacer."""
        
        if messagebox.askyesno("🗑️ Confirmar eliminación", confirm_msg):
            # Obtener índice del elemento seleccionado
            index = self.events_tree.index(item)
            
            # Eliminar de la lista global
            global lista
            if 0 <= index < len(lista):
                evento_eliminado = lista[index]
                del lista[index]
                
                # Guardar cambios
                if DataManager.save_events(lista):
                    messagebox.showinfo("✅ Éxito", 
                                      f"Evento '{evento_nombre}' eliminado correctamente")
                    self.load_and_display_events()
                    self.show_info_message("Evento eliminado. Selecciona otro para ver detalles.")
                else:
                    # Restaurar evento si falla el guardado
                    lista.insert(index, evento_eliminado)
                    messagebox.showerror("❌ Error", "No se pudo eliminar el evento")

    def export_events(self):
        """Exporta eventos con opciones"""
        try:
            filename = AdvancedFeatures.export_events_to_csv()
            if filename:
                messagebox.showinfo("💾 Exportación exitosa", 
                                  f"Datos exportados correctamente a:\n{filename}")
            else:
                messagebox.showerror("❌ Error de exportación", 
                                   "No se pudieron exportar los datos")
        except Exception as e:
            messagebox.showerror("❌ Error", f"Error al exportar: {str(e)}")

    def new_event(self):
        """Crea un nuevo evento"""
        self.wind.destroy()
        root = Tk()
        root.configure(bg=ModernColors.BACKGROUND)
        app = ModernCalendar(root)
        root.mainloop()

    def go_back(self):
        """Vuelve a la ventana principal"""
        self.wind.destroy()
        root = Tk()
        root.configure(bg=ModernColors.BACKGROUND)
        app = ModernMainWindow(root)
        root.mainloop()

# Alias para compatibilidad
recordatorio = ModernReminders


class recordatorio:
    def __init__(self, windowRemember):
        self.windRemember = windowRemember
        self.windRemember.geometry("1100x650")
        self.windRemember.title('Agenda')
        self.windRemember.configure(bg=ModernColors.BACKGROUND)
        self.iniciarArchivo()
        self.cargar()
        self.content()

    def iniciarArchivo(self):
        archivo = open("recordatorio.txt", "a")
        archivo.close()

    def cargar(self):
        archivo = open("recordatorio.txt", "r")
        linea = archivo.readline()
        if linea:
            while linea:
                if linea[-1] == "\n":
                    linea = linea[:-1]
                lista.append(linea)
                linea = archivo.readline()
        archivo.close()

    
    def content(self):
        label = Label(
            self.windRemember,
        )
        label.place(x=0, y=0)
        Label(self.windRemember, text="Lista de Eventos", font=("Helvetica", 16), foreground=("red"), bg=ModernColors.BACKGROUND).pack(pady=20)
        def consultar():
            r = Text(self.windRemember, width=250, height=18)
            lista.sort()
            valores = []
            r.insert(INSERT, "Fecha\t\tEvento\t\tNombre\t\tHora\t\tMinutos\t\tHora\t\tMinutos\t\tTiempo Invertido\t\tObservación\n")
            for elemento in lista:
                arreglo = elemento.split("$")
                valores.append(arreglo[5])
                r.insert(INSERT, arreglo[0]+"\t\t"+arreglo[1]+"\t\t"+arreglo[2]+"\t\t"+arreglo[3]+"\t\t"+arreglo[4]+"\t\t"
                        +arreglo[5]+"\t\t"+arreglo[6]+"\t\t"+arreglo[7]+"\t\t"+arreglo[8]+"\n")
                r.place(x=50, y=80)
                delete = Spinbox(self.windRemember, value=(valores), textvariable=conteliminar)
                delete.place(x=380, y=450)
            if lista == []:
                delete = Spinbox(self.windRemember, value=(valores))
                delete.place(x=380, y=450)
            r.config(state=DISABLED)


        conteliminar = StringVar()
        def escribirEvento():
            archivo = open("recordatorio.txt", "w")
            lista.sort()
            for elemento in lista:
                archivo.write(elemento + "\n")
            archivo.close()
            
        def eliminar():
            conteliminar.get()
            removido = False
            for elemento in lista:
                arreglo = elemento.split("$")
                if conteliminar.get() == arreglo[2]:
                    lista.remove(elemento)
                    removido = True
            escribirEvento()
            consultar()
            if removido:
                messagebox.showinfo("Eliminar", "Elemento eliminado" + " " + conteliminar.get())

        Label(self.windRemember, text="Escribe el nombre del evento para eliminar", font=("Helvetica", 16), foreground=("red"), bg=ModernColors.BACKGROUND).place(x=250, y=400)
        delete = Entry(self.windRemember, textvariable=conteliminar)
        delete.place(x=380, y=450)

        btnEliminar = Button(self.windRemember, text="Eliminar", command=eliminar, width=20, height=1, font=('Helvetica', 16), bg='#0052cc', fg='#ffffff', activebackground='#0052cc', activeforeground='#aaffaa')
        btnEliminar.place(x=330, y=480)

        def index1():
            self.windRemember.destroy()
            obj = index(Tk())
            obj.wind.mainloop()
        btnAtrás =Button(self.windRemember, text="Atrás", command=index1, width=20, height=1, font=('Helvetica', 16), bg='#0052cc', fg='#ffffff', activebackground='#0052cc', activeforeground='#aaffaa')
        btnAtrás.place(x=330, y=530)

        consultar()

if __name__ == "__main__":
    # Configurar el estilo moderno
    ModernStyleUtils.configure_modern_style()
    
    # Crear ventana principal
    root = Tk()
    root.configure(bg=ModernColors.BACKGROUND)
    
    # Inicializar aplicación
    app = ModernMainWindow(root)
    
    # Ejecutar aplicación
    root.mainloop()