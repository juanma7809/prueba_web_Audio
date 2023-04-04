const btn = document.getElementById('btn--hamburguesa');
const menu = document.getElementById('menu');
const logout = document.getElementById('navbar--logout');



let mediaRecorder;
let recordedChunks = [];

btn.addEventListener('click',()=>{
    menu.classList.toggle('diplay-menu');
    logout.classList.toggle('diplay-logout');
});

window.addEventListener('load',()=>{
    if(window.innerWidth > 768){
        menu.style.display = 'block'
        logout.style.display = 'flex'
    }
});

navigator.mediaDevices.getUserMedia({ audio: true, video: true })
  .then(stream => {
    // Obtener el elemento de video y mostrar el flujo de video en él
    const video = document.getElementById('video');
    video.srcObject = stream;
    //video.play();
    
    // Crear una instancia de MediaRecorder para grabar el flujo de video
    mediaRecorder = new MediaRecorder(stream, { mimeType: 'video/webm' });
    
    // Agregar los chunks grabados al arreglo recordedChunks
    mediaRecorder.ondataavailable = e => {
      recordedChunks.push(e.data);
    };
    
    // Guardar el archivo de video cuando se detiene la grabación
    mediaRecorder.onstop = () => {
      const blob = new Blob(recordedChunks, { type: 'video/webm' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      document.body.appendChild(a);
      a.style = 'display: none';
      a.href = url;
      a.download = 'captura.mp4';
      a.click();
      window.URL.revokeObjectURL(url);
    };
  })
  .catch(err => {
    console.error('Error al obtener acceso a la cámara y el micrófono:', err);
  });

// Iniciar la grabación del video cuando se hace clic en el botón de grabar
document.getElementById('boton-grabar').addEventListener('click', () => {
  recordedChunks = [];
  mediaRecorder.start();
  video.play();
});

// Detener la grabación del video cuando se hace clic en el botón de detener
document.getElementById('boton-detener').addEventListener('click', () => {
  mediaRecorder.stop();
});
