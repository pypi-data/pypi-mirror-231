__title__ = 'logobj'
__summary__ = 'Poorman\'s inspection debugger'
__author__ = 'Michael Loyd'
__email__ = 'michael@loyd.org'
__version__ = '0.0.1'
__license__ = 'MIT'
__copyright__ = "Copyright 2022 %s" % __author__


import inspect, shutil, json
from pprint import pformat as _pformat

COLS, ROWS = shutil.get_terminal_size((120, 80))
# COLS -= 35
NoneType = type(None)


def logobj(obj, name=None, logger=print, obj_doc=True, multi_line_doc=False):
    debug = logger
    if hasattr(debug, 'debug'):
        debug = debug.debug

    debug(f'{"=" * 5} {name or "logobj"} {"=" * COLS * 2}'[:COLS])
    otype = type(obj)
    otname = f'{otype.__module__}.{otype.__name__}'
    debug(f'obj {otname}')
    try:
        debug(f'file: {inspect.getfile(otype)}')
    except TypeError:
        pass

    if obj_doc:
        doc = (
            inspect.getdoc(otype)
            or inspect.getcomments(otype)
            or inspect.getcomments(obj)
            or 'No doc or coment'
        )
        if '\n' in doc:
            doc = '\n'.join(f'  {ln}' for ln in doc.split('\n'))
        debug(doc)

    gentle_items = {
        'aiohttp.client_reqrep.ClientResponse': ['ok'],
        'constructs.Node': ['PATH_SEP'],
        'aws_cdk.aws_codebuild.Project': ['connections'],
    }

    attr_prefix_avoid = '_' if otname == 'importlib.metadata.PackagePath' else '__'
    mnames = [
        attr
        for attr in dir(obj)
        if not attr.startswith(attr_prefix_avoid)
        and attr not in gentle_items.get(otname, [])
    ]
    members = []
    for attr in mnames:
        # print(f'attr: {attr!r}')
        members.append((attr, getattr(obj, attr)))

    gutter = max(20, max(len(attr) for attr, _ in members) if members else 20)

    is_a_funcs = [
        (name[2:], func)
        for name in dir(inspect)
        if name.startswith('is')
        and (func := getattr(inspect, name))  # noqa
        and inspect.isfunction(func)          # noqa
    ]
    for attr, val in members:
        val = 'gentle' if attr in gentle_items else val
        line = f'{attr: <{gutter}}'
        val_type = type(val)
        mname = val_type.__module__
        tname = val_type.__name__ if val_type.__name__ not in ('builtin_function_or_method',) else ''
        type_desc = f'{mname}.' if mname != 'builtins' else ''
        type_desc += tname

        if val_type in (NoneType, bool, int):
            line += repr(val)
            debug(line[:COLS])
            continue

        if val_type in (str,) or type_desc in ('yarl.URL'):
            line += f'{str(val)!r}'
            debug(line[:COLS])
            continue

        isables = ', '.join(name for name, func in is_a_funcs if func(val))
        if isables:
            line += f'({isables}) '

        if type_desc not in isables:
            line += type_desc + ' '

        if isinstance(val, dict):
            line += '{'
            entries = []
            for dkey, dval in val.items():
                parts = []
                for part in (dkey, dval):
                    if isinstance(part, (NoneType, str, int)):
                        parts.append(repr(part))
                    else:
                        parts.append(type(part).__name__)
                entries.append(':'.join(parts))
            line += ', '.join(entries)
            line += '}'
        elif isinstance(val, (list, set, tuple)):
            line += '('
            line += ', '.join(
                repr(part)
                if isinstance(part, (NoneType, str, int))
                else type(part).__name__
                for part in val
            )
            line += ')'
        else:
            doc = (
                inspect.getdoc(val)
                or inspect.getcomments(val)
                or ''
            ).strip()
            if doc:
                doc = doc.split('\n')
                line += ': ' + doc[0]
                doc = doc[1:] if multi_line_doc else []
                while doc:
                    if line[:COLS].strip():
                        debug(line[:COLS])
                    line = f'{" ": <{gutter}}' + doc[0]
                    doc = doc[1:]

        debug(line[:COLS])

    debug(f'{"=" * 50}')


class JSONDatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            return super().default(obj)
        except TypeError:
            if hasattr(obj, 'isoformat'):
                try:
                    return obj.isoformat(timespec='microseconds')
                except TypeError:
                    return obj.isoformat()
            raise


def dumps(*args, **kwargs):
    return json.dumps(*args, **kwargs, cls=JSONDatetimeEncoder)


def pformat(*args, **kwargs):
    try:
        indent = kwargs.pop('indent', 2)
        cls = kwargs.pop('cls', JSONDatetimeEncoder)
        return json.dumps(*args, indent=indent, cls=cls, **kwargs)
    except TypeError as err:
        print(err)

    return _pformat(*args, **kwargs)
