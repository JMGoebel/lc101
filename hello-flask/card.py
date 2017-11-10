from jinja2 import Template

def card(name, title, content):
    style = "color: red; background-color: yellow;"
    
    template = Template(
        '''
        <div class="card" style="{{ style }}">
            <h1>{{ title }}</h1>
            <h3>{{ name }}</h3>
            <p>{{ content }}</p>
        </div>
        '''
    )

    return template.render(name = name,
                           style = style,
                           title = title,
                           content = content )