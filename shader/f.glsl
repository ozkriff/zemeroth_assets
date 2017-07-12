uniform vec4 u_Basic_color;
uniform sampler2D t_Tex;
varying vec2 v_Uv;

void main() {
    gl_FragColor = u_Basic_color * texture2D(t_Tex, v_Uv);
}
