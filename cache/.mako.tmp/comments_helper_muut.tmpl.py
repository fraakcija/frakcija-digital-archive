# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1575321474.822212
_enable_loop = True
_template_filename = '/usr/local/lib/python3.6/dist-packages/nikola/data/themes/base/templates/comments_helper_muut.tmpl'
_template_uri = 'comments_helper_muut.tmpl'
_source_encoding = 'utf-8'
_exports = ['comment_form', 'comment_link', 'comment_link_script']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_form(context,url,title,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <a class="muut" href="https://muut.com/i/')
        __M_writer(str(comment_system_id))
        __M_writer('/')
        __M_writer(str(identifier))
        __M_writer('">')
        __M_writer(str(comment_system_id))
        __M_writer(' forums</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\n<script src="https://cdn.muut.com/1/moot.min.js"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/usr/local/lib/python3.6/dist-packages/nikola/data/themes/base/templates/comments_helper_muut.tmpl", "uri": "comments_helper_muut.tmpl", "source_encoding": "utf-8", "line_map": {"16": 0, "21": 2, "22": 5, "23": 8, "24": 13, "30": 3, "35": 3, "36": 4, "37": 4, "38": 4, "39": 4, "40": 4, "41": 4, "47": 7, "51": 7, "57": 11, "61": 11, "67": 61}}
__M_END_METADATA
"""
