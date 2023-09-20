def python_formatter(template_string, _context):
    try:
        return template_string.format(**_context)
    except Exception:
        raise
