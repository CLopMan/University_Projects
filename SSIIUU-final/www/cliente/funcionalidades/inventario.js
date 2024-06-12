import { init_fav, favorito } from "./favorito.js";
import { socket, name } from "../script.js";

// Declaramos las constantes del programa

const ANCHO_FIGURA = 2;
const ALTURA_FIGURA = 3;
const FILAS_MATRIZ = 10;
const COLUMNAS_MATRIZ = 8;
const COLOR_FIGURAS_BOLLO = "#aa6a3b";
const COLOR_FIGURAS_CREMA = "#a588db";
const COLOR_FIGURAS_BOLLO_COLOCADAS = "#7f3f2c";
const COLOR_FIGURAS_CREMA_COLOCADAS = "#7966b9";
const COLOR_FIGURA_SELECCIONADA = "#a52230";
const COLOR_FONDO = "#3c2012";
const modal_tetris = document.getElementById("modal_tetris");

/**
 * Clase que corresponde con las figuras del tetris
 * @param {int} id - Id que corresponde a la figura, relaciona la figura con el id en el json
 * @param {int} x - Posición x de la figura
 * @param {int} y - Posición y de la figura
 * @param {int} height - Altura de la figura
 * @param {int} widht - Anchura de la figura
 * @param {bool} favorito - Si esta figura es favorito o no
 * @param {string} tipo - Tipo de objeto al que corresponde la figura
 */

class Figura {
    constructor(id, x, y, height, width, favorito, tipo) {
        this.id = id;
        this.height = height;
        this.width = width;
        this.orientacion = 0;
        this.x = x;
        this.y = y;
        this.colocada = false;
        this.favorito = favorito;
        this.tipo = tipo;

        if (tipo == "bollo") {
            this.precio = 2;
            this.color = COLOR_FIGURAS_BOLLO;
        } else {
            this.precio = 15.94;
            this.color = COLOR_FIGURAS_CREMA;
        }
    }
}

// Declaración de array de figuras y de array de objetos que relacionan la figura con su div
let lista_figuras = [];
let div_figuras = [];

// Declaración de la matriz del tetris
const matriz_figuras = [];
for (let i = 0; i < FILAS_MATRIZ; i++) {
    matriz_figuras.push(new Array(COLUMNAS_MATRIZ).fill(0));
}

// Variable que indica cual debe de ser el siguiente id de la siguiente figura
let id_actual = 0;

// Variable local de la lectura del json
export let json;

let figura_actual;
let figura_seleccionada;
let draw_id;
let move_id;
export let num = { num: 0 };

// Generar las celdas del juego de Tetris
const grid = document.getElementById("grid");
let cells = [];
for (let i = 0; i < FILAS_MATRIZ; i++) {
    for (let j = 0; j < COLUMNAS_MATRIZ; j++) {
        const cell = document.createElement("div");
        cell.classList.add("cell");
        grid.appendChild(cell);
        cells.push(cell);
    }
}

/**
 * Función que envía un mensaje al servidor para leer el json
 */
export function leer_estado() {
    reset_inventory();
    socket.emit("LOAD_STATE");
}

/**
 * Tras recibir el json se vuelca el contenido de este en el tetris
 * @param {object} data - Contenido del json
 */
export function cargar_estado(data) {
    set_up();

    // Cargas el estado
    let key_id = 0;
    json = data;
    Object.keys(data).forEach((key) => {
        key_id = key;
        figura_actual = new Figura(
            key,
            data[key].x,
            data[key].y,
            data[key].height,
            data[key].width,
            data[key].fav,
            data[key].tipo
        );
        lista_figuras.push(figura_actual);
        colocarBloque(figura_actual.favorito);
    });
    id_actual = Number(key_id) + 1;
    init_fav();
}

/**
 * Recarga el tetris a su estado original
 */
export function reset_inventory() {
    // Reinicias el inventario
    for (let i = 0; i < FILAS_MATRIZ; i++) {
        matriz_figuras[i].fill(0);
    }

    for (let div of div_figuras) {
        div["div_figura"].remove();
    }

    figura_seleccionada = null;

    window.clearInterval(draw_id);
    window.clearInterval(move_id);

    lista_figuras = [];
    div_figuras = [];
}

/**
 * Función que envía un mensaje al servidor, enviando el json
 */
export function escribir_estado() {
    socket.emit("STORE_STATE", json, name);
}

/**
 * Coloca 1's en la matriz del tetris en la posición de la figura actual
 */
function dibujarFiguraEnMatriz() {
    for (let i = 0; i < figura_actual.height; i++) {
        for (let j = 0; j < figura_actual.width; j++) {
            matriz_figuras[figura_actual.y + i][figura_actual.x + j] = 1;
        }
    }
}

/**
 * Coloca 0's en la matriz del tetris en la posición de la figura
 * @param {Figura} figura - Figura a borrar en la matriz
 */
function borrarFiguraEnMatriz(figura) {
    for (let i = 0; i < figura.height; i++) {
        for (let j = 0; j < figura.width; j++) {
            matriz_figuras[figura.y + i][figura.x + j] = 0;
        }
    }
}

/**
 * Se encarga de colocar el bloque y todo lo que conlleva
 ** Vibrar
 ** Crear un div superior para la selección de la figura
 ** Añadir el sistema de favoritos
 ** Escribir en la variable json la nueva figura
 * @param {bool} fav
 */
function colocarBloque(fav) {
    if (figura_actual.tipo == "bollo") {
        figura_actual.color = COLOR_FIGURAS_BOLLO_COLOCADAS;
    } else {
        figura_actual.color = COLOR_FIGURAS_CREMA_COLOCADAS;
    }
    window.navigator.vibrate(100);

    let div_figura = divFigura();

    let div_fav = divFavorito(div_figura, fav);

    favorito["favourite_list"][div_figura.id] = {
        favorito: fav,
        contador: 0,
        estrella: div_fav,
    };

    dibujarFiguraEnMatriz();

    json[figura_actual.id] = {
        tipo: figura_actual.tipo,
        fav: fav,
        x: figura_actual.x,
        y: figura_actual.y,
        height: figura_actual.height,
        width: figura_actual.width,
        precio: figura_actual.precio,
    };
    escribir_estado();
    figura_actual = null;
    modal_tetris.style.display = "none";
    num["num"] += 1;
}

/**
 * Crea un div tranparente por encima de la figura actual
 * @returns Devuelve el div que corresponde a la figura
 */
function divFigura() {
    let index_top_left = figura_actual.y * COLUMNAS_MATRIZ + figura_actual.x;
    let index_bottom_right =
        (figura_actual.y + figura_actual.height - 1) * COLUMNAS_MATRIZ +
        figura_actual.x +
        figura_actual.width -
        1;

    let celda_top_left = cells[index_top_left];
    let celda_bottom_right = cells[index_bottom_right];

    let rect_top_left = celda_top_left.getBoundingClientRect();
    let rect_bottom_right = celda_bottom_right.getBoundingClientRect();

    let div_figura = document.createElement("div");

    let width = rect_bottom_right.right - rect_top_left.left;
    let height = rect_bottom_right.bottom - rect_top_left.top;

    div_figura.id = figura_actual.id;

    div_figura.style.position = "absolute";
    div_figura.style.left = rect_top_left.left + "px";
    div_figura.style.top = rect_top_left.top + "px";
    div_figura.style.width = width + "px";
    div_figura.style.height = height + "px";

    document.body.appendChild(div_figura);
    div_figuras.push({ div_figura, figura_actual });
    div_figura.addEventListener("touchend", () => {
        handle_touch(div_figura);
    });
    return div_figura;
}

/**
 * Se encarga de gestionar los toques realizados a div_figura para seleccionarla
 * @param {HTMLElement} div_figura
 */
function handle_touch(div_figura) {
    let par_figura_div;
    // Si se vuelve a tocar la misma se deselecciona
    if (figura_seleccionada === div_figura) {
        par_figura_div = div_figuras.find(
            (elemento) => elemento.div_figura === div_figura
        );
        if (par_figura_div.figura_actual.tipo == "bollo") {
            par_figura_div.figura_actual.color = COLOR_FIGURAS_BOLLO_COLOCADAS;
        } else {
            par_figura_div.figura_actual.color = COLOR_FIGURAS_CREMA_COLOCADAS;
        }
        figura_seleccionada = null;
        favorito.div_id = null;

        // Si se toca cualquier otra se selecciona y la anterior deja de estar seleccionada
    } else {
        par_figura_div = div_figuras.find(
            (elemento) => elemento.div_figura === div_figura
        );
        if (figura_seleccionada) {
            let par_figura_div_select = div_figuras.find(
                (elemento) => elemento.div_figura === figura_seleccionada
            );
            if (par_figura_div_select.figura_actual.tipo == "bollo") {
                par_figura_div_select.figura_actual.color = COLOR_FIGURAS_BOLLO_COLOCADAS;
            } else {
                par_figura_div_select.figura_actual.color = COLOR_FIGURAS_CREMA_COLOCADAS;
            }
        }
        par_figura_div.figura_actual.color = COLOR_FIGURA_SELECCIONADA;
        figura_seleccionada = div_figura;
        favorito.div_id = figura_seleccionada.id;
    }
}

/**
 * Se encarga de deseleccionar una figura si realiza el favorito
 * @param {HTMLElement} div_id
 */
export function deseleccionar_objeto(div_id) {
    let div_figura = document.getElementById(div_id);
    let par_figura_div = div_figuras.find(
        (elemento) => elemento.div_figura === div_figura
    );

    if (par_figura_div.figura_actual.tipo == "bollo") {
        par_figura_div.figura_actual.color = COLOR_FIGURAS_BOLLO_COLOCADAS;
    } else {
        par_figura_div.figura_actual.color = COLOR_FIGURAS_CREMA_COLOCADAS;
    }
    figura_seleccionada = null;
    favorito.div_id = null;
}

/**
 * Se encarga de crear un div que corresponde a la respuesta visual de marcar como favorito un objeto
 * @param {HTMLElement} div_figura
 * @param {bool} favorito
 * @returns {HTMLElement} div de favorito
 */
function divFavorito(div_figura, favorito) {
    let div_pequeno = document.createElement("div");

    div_pequeno.style.position = "relative";
    div_pequeno.style.right = "0px";
    div_pequeno.style.top = "0px";
    div_pequeno.style.width = "20px";
    div_pequeno.style.height = "20px";
    if (favorito == true) {
        div_pequeno.style.backgroundColor = "yellow";
    }
    div_pequeno.style.zIndex = "100";
    div_pequeno.setAttribute("class", "favorito");

    div_figura.appendChild(div_pequeno);

    return div_pequeno;
}
/**
 * Se encarga de eleminar la figura actualmente seleccionada, tando de la parte lógica del tetris como de la parte visual
 * y además de escribir el json este cambio
 * @returns
 */
function eliminarFigura() {
    if (
        !figura_seleccionada ||
        favorito["favourite_list"][figura_seleccionada.id]["favorito"] == 1
    ) {
        return;
    }

    let par_figura_div = div_figuras.find(
        (elemento) => elemento.div_figura === figura_seleccionada
    );

    par_figura_div.div_figura.parentNode.removeChild(par_figura_div.div_figura);
    figura_seleccionada = null;

    borrarFiguraEnMatriz(par_figura_div.figura_actual);
    lista_figuras = lista_figuras.filter(
        (figura) => figura !== par_figura_div.figura_actual
    );

    let id = par_figura_div.figura_actual.id;
    let json_copy = {};
    Object.keys(json).forEach((i) => {
        if (id != i) {
            json_copy[i] = json[i];
        }
    });
    json = json_copy;
    num["num"] -= 1;
    escribir_estado();
}

/**
 * Mueve la figura actual hacia la izquierda si es posible
 */
function moverFiguraIzquierda() {
    if (figura_actual.x + figura_actual.width < COLUMNAS_MATRIZ) {
        let colision = false;
        for (let i = 0; i < figura_actual.height && !colision; i++) {
            if (
                matriz_figuras[figura_actual.y + i][
                    figura_actual.x + figura_actual.width
                ] === 1
            ) {
                colision = true;
            }
        }
        if (!colision) {
            figura_actual.x++;
        }
    }
}
/**
 * Mueve la figura actual hacia la derecha si es posible
 */
function moverFiguraDerecha() {
    if (figura_actual.x > 0) {
        let colision = false;
        for (let i = 0; i < figura_actual.height && !colision; i++) {
            if (matriz_figuras[figura_actual.y + i][figura_actual.x - 1] === 1) {
                colision = true;
            }
        }
        if (!colision) {
            figura_actual.x--;
        }
    }
}
/**
 * Mueve la figura hacia abajo si es posible, en caso contrario coloca el bloque actual
 * @returns
 */
function moverFiguraAbajo() {
    if (!figura_actual) {
        return;
    }
    if (!colisionAbajo()) {
        figura_actual.y++;
        // Actualizar visualización o lógica relacionada con el movimiento
    } else {
        // La figura ha llegado al final, puedes hacer algo aquí como colocarla o generar una nueva figura.
        colocarBloque(false);
    }
}
/**
 * Evalua el estado de la figura actual para indicar si colisiona en la parte inferior de la figura
 * o no
 * @returns {bool} Colisiona o no colisiona
 */
function colisionAbajo() {
    if (figura_actual.y + figura_actual.height >= FILAS_MATRIZ) {
        return true;
    }
    for (let i = 0; i < figura_actual.width; i++) {
        if (
            matriz_figuras[figura_actual.y + figura_actual.height][
                figura_actual.x + i
            ] === 1
        ) {
            return true;
        }
    }
    return false;
}

/**
 * Rota la figura actual hacia la derecha, generando una nueva matriz con la figura rotada,
 * si esta nueva figura colisiona con otra no se realizará la rotación
 */
function rotarFiguraDerecha() {
    const nuevaAltura = figura_actual.width;
    const nuevaAnchura = figura_actual.height;
    const nuevaMatriz = [];
    for (let i = 0; i < nuevaAltura; i++) {
        nuevaMatriz[i] = [];
        for (let j = 0; j < nuevaAnchura; j++) {
            nuevaMatriz[i][j] =
                matriz_figuras[figura_actual.y + j][
                    figura_actual.x + nuevaAnchura - i - 1
                ];
        }
    }
    if (!hayColision(nuevaMatriz)) {
        figura_actual.height = nuevaAltura;
        figura_actual.width = nuevaAnchura;
        figura_actual.orientacion = (figura_actual.orientacion + 1) % 4;
        for (let i = 0; i < nuevaAltura; i++) {
            for (let j = 0; j < nuevaAnchura; j++) {
                matriz_figuras[figura_actual.y + i][figura_actual.x + j] =
                    nuevaMatriz[i][j];
            }
        }
    }
}

/**
 * Rota la figura actual hacia la izquierda, generando una nueva matriz con la figura rotada,
 * si esta nueva figura colisiona con otra no se realizará la rotación
 */
function rotarFiguraIzquierda() {
    const nuevaAltura = figura_actual.width;
    const nuevaAnchura = figura_actual.height;
    const nuevaMatriz = [];
    for (let i = 0; i < nuevaAltura; i++) {
        nuevaMatriz[i] = [];
        for (let j = 0; j < nuevaAnchura; j++) {
            nuevaMatriz[i][j] =
                matriz_figuras[figura_actual.y + nuevaAltura - j - 1][
                    figura_actual.x + i
                ];
        }
    }
    if (!hayColision(nuevaMatriz)) {
        figura_actual.height = nuevaAltura;
        figura_actual.width = nuevaAnchura;
        figura_actual.orientacion = (figura_actual.orientacion + 3) % 4;
        for (let i = 0; i < nuevaAltura; i++) {
            for (let j = 0; j < nuevaAnchura; j++) {
                matriz_figuras[figura_actual.y + i][figura_actual.x + j] =
                    nuevaMatriz[i][j];
            }
        }
    }
}

/**
 * Evalua el estado de una nueva Matriz con una figura rotada
 * @param {Array<Array>} nuevaMatriz
 * @returns Colisiona o no colisiona
 */
function hayColision(nuevaMatriz) {
    for (let i = 0; i < nuevaMatriz.length; i++) {
        for (let j = 0; j < nuevaMatriz[i].length; j++) {
            if (
                nuevaMatriz[i][j] === 1 &&
                (figura_actual.y + i >= FILAS_MATRIZ ||
                    figura_actual.x + j >= COLUMNAS_MATRIZ ||
                    figura_actual.y + i < 0 ||
                    figura_actual.x + j < 0 ||
                    matriz_figuras[figura_actual.y + i][figura_actual.x + j] === 1)
            ) {
                return true;
            }
        }
    }
    return false;
}

/**
 * Genera un nuevo bloque en el grid del tetris según el tipo especificado
 * y lo añade a la lista de figuras
 * @param {string} tipo - tipo de la nueva figura
 */
export function generar_bloque(tipo) {
    modal_tetris.style.display = "block";
    figura_actual = new Figura(id_actual, 3, 0, ALTURA_FIGURA, ANCHO_FIGURA, 0, tipo);
    id_actual += 1;
    lista_figuras.push(figura_actual);
}

/** Dibuja las figuras que se encuentren en lista_figuras
 ** Pinta todas las celdas del color del fondo
 ** Pinta cada una de las figuras de lista_figuras
 */
function dibujar_figuras() {
    for (let cell of cells) {
        cell.style.backgroundColor = COLOR_FONDO;
        cell.style.backgroundImage = "none";
    }
    for (let figura of lista_figuras) {
        for (let i = 0; i < figura.height; i++) {
            for (let j = 0; j < figura.width; j++) {
                if (
                    figura.y + i >= 0 &&
                    figura.y + i < FILAS_MATRIZ &&
                    figura.x + j >= 0 &&
                    figura.x + j < COLUMNAS_MATRIZ
                ) {
                    const index = (figura.y + i) * COLUMNAS_MATRIZ + (figura.x + j);
                    cells[index].style.backgroundColor = figura.color;
                    cells[
                        index
                    ].style.backgroundImage = `url('imagenes/${figura.tipo}.png')`;
                    cells[index].style.backgroundSize = "cover";
                }
            }
        }
    }
}

/**
 * Se encarga de inicializar todo lo necesario para el funcionamiento del tetris
 ** Intervalos de dibujado y movimiento
 ** Crear el listener de movimiento para detectar gestos
 */
function set_up() {
    draw_id = setInterval(dibujar_figuras, 50);
    move_id = setInterval(moverFiguraAbajo, 1500);
    let startAngle = {};
    let startTime = null;
    let isLocked = false; // nuevo estado de bloqueo
    const lockTimeMS = 500; // tiempo de bloqueo después de detectar un giro
    window.addEventListener("deviceorientation", handleOrientation, true);

    function handleOrientation(event) {
        if (isLocked) return;

        const currentAngle = {
            alpha: event.alpha,
            beta: event.beta,
            gamma: event.gamma,
        };
        if (
            (currentAngle.beta > 160 && currentAngle.beta < 190) ||
            (currentAngle.beta < -160 && currentAngle.beta > -190)
        ) {
            eliminarFigura();
        }
        const minRotacionAlpha = 30;
        const minRotacionGamma = 50;

        const movementTimeMS = 300;

        const currentTime = new Date().getTime();

        if (!figura_actual) return;
        if (startTime === null) {
            // inicializar
            startAngle = { ...currentAngle };
            startTime = currentTime;
        } else {
            const AngleDiff = {};
            AngleDiff.alpha = currentAngle.alpha - startAngle.alpha;
            AngleDiff.beta = currentAngle.beta - startAngle.beta;
            AngleDiff.gamma = currentAngle.gamma - startAngle.gamma;

            const timeDiff = currentTime - startTime;

            if (AngleDiff.alpha >= minRotacionAlpha && timeDiff <= movementTimeMS) {
                // derecha
                moverFiguraDerecha();
                dibujar_figuras();

                isLocked = true; // bloquear la detección de giros
                setTimeout(() => {
                    isLocked = false; // desbloquear después de lockTimeMS
                }, lockTimeMS);
                startAngle = { ...currentAngle };
                startTime = currentTime;
            } else if (
                AngleDiff.alpha < -minRotacionAlpha &&
                timeDiff <= movementTimeMS
            ) {
                // izquierda
                moverFiguraIzquierda();
                dibujar_figuras();

                isLocked = true; // bloquear la detección de giros
                setTimeout(() => {
                    isLocked = false; // desbloquear después de lockTimeMS
                }, lockTimeMS);
                startAngle = { ...currentAngle };
                startTime = currentTime;
            } else if (
                AngleDiff.gamma >= minRotacionGamma &&
                timeDiff <= movementTimeMS
            ) {
                // rotar derecha
                rotarFiguraDerecha();
                dibujar_figuras();

                isLocked = true; // bloquear la detección de giros
                setTimeout(() => {
                    isLocked = false; // desbloquear después de lockTimeMS
                }, lockTimeMS);
                startAngle = { ...currentAngle };
            } else if (
                AngleDiff.gamma < -minRotacionGamma &&
                timeDiff <= movementTimeMS
            ) {
                //rotar izquierda
                rotarFiguraIzquierda();
                dibujar_figuras();
                isLocked = true; // bloquear la detección de giros
                setTimeout(() => {
                    isLocked = false; // desbloquear después de lockTimeMS
                }, lockTimeMS);
                startAngle = { ...currentAngle };
            } else if (timeDiff > movementTimeMS) {
                // se ha pasado el tiempo
                startAngle = { ...currentAngle };
                startTime = currentTime;
            }
        }
    }
}
