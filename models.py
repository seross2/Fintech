def calcular_riesgo_crediticio(salario_smmlv: float, tiene_reportes: bool, anos_historial: int) -> str:
    """Evalúa el riesgo basado en las políticas de FinTech Andina."""
    
    # Regla 1: < 2 SMMLV Y reportes negativos
    if salario_smmlv < 2 and tiene_reportes:
        return "Rechazado"
    
    # Regla 2: > 4 SMMLV O (> 5 años de historial SIN reportes)
    if salario_smmlv > 4 or (anos_historial > 5 and not tiene_reportes):
        return "Aprobado Automáticamente"
    
    # Regla 3: Cualquier otro caso
    return "Revisión Manual"