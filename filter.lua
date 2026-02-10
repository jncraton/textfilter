local function remove_attrs(el)
  if el.attr then
    el.attr = pandoc.Attr()
  end
  if el.title then
    el.title = ''
  end
  return el
end

function RawBlock(el)
  return {}
end

function RawInline(el)
  return {}
end

function Image(el)
  return {}
end

function Figure(el)
  return {}
end

function Span(el)
  return el.content
end

function Emphasis(el)
  return el.content
end

function Strong(el)
  return el.content
end

function SoftBreak()
  return pandoc.Space()
end

function Div(el)
  return el.content
end

function Note(el)
  return {}
end

function Cite(el)
  return {}
end

function Header(el)
  return remove_attrs(el)
end

function Link(el)
  for _, v in ipairs(el.content) do
    if v.t ~= 'Image' then
      return remove_attrs(el)
    end
  end
  return {}
end

function Code(el)
  return remove_attrs(el)
end

function Str(el)
  el.text = el.text:gsub('\u{a0}+', ' ')
  return el
end

function CodeBlock(el)
  return remove_attrs(el)
end

function Para(el)
  remove_attrs(el)
  local inls = el.content
  if #inls == 0 then
    return nil
  end

  local last = inls[#inls]

  if last.t == 'Str' then
    if last.text:sub(-1) == '.' then
      last.text = last.text:sub(1, -2)
      inls[#inls] = last
    end
  end

  return el
end

function Plain(el)
  return remove_attrs(el)
end

function BulletList(el)
  return remove_attrs(el)
end

function OrderedList(el)
  return remove_attrs(el)
end

function DefinitionList(el)
  return remove_attrs(el)
end

function Table(el)
  return remove_attrs(el)
end
