# Copyright (C) 2017 Jurriaan Bremer.
# This file is part of SFlock - http://www.sflock.org/.
# See the file 'docs/LICENSE.txt' for copying permission.

from sflock.main import unpack

def test_doc1():
    f = unpack("tests/files/doc_1.docx_")
    assert f.duplicate is False
    assert f.selected is True
    assert f.preview is False
    assert f.package == "doc"
    assert f.get_child("[Content_Types].xml") is not None
    assert len(f.children) == 12
    assert f.children[0].selected is False
    assert f.children[4].selected is False
    assert f.children[8].selected is False
    assert f.children[11].selected is False

def test_doc2():
    f = unpack("tests/files/doc_2.xlsx_")
    assert f.duplicate is False
    assert f.selected is True
    assert f.preview is False
    assert f.package == "xls"
    assert f.get_child("[Content_Types].xml") is not None
    assert len(f.children) == 12
    assert f.children[0].selected is False
    assert f.children[11].selected is False
