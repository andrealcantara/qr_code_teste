$(function(){
    const args = {
        video: $("#preview")[0],
        scanPeriod: 5,
        mirror: false
    };
    window.URL.createObjectURL = (stream) => {
        args.video.srcObject = stream;
        return stream;
    };
    let scanner = new Instascan.Scanner(args);
    scanner.addListener('scan', function (content) {
        alert(content);
        //window.location.href=content;
    });

    Instascan.Camera.getCameras().then(function (cameras) {
        if (cameras.length > 0) {
            if(cameras.length > 1)
                scanner.start(cameras[1]);
            else
                scanner.start(cameras[0]);
            $('[name="options"]').on('change', function () {
                if ($(this).val() == 1) {
                    if (cameras[0] != "") {
                        scanner.start(cameras[0]);
                    } else {
                        alert('No Front camera found!');
                    }
                } else if ($(this).val() == 2) {
                    if (cameras[1] != "") {
                        scanner.start(cameras[1]);
                    } else {
                        alert('No Back camera found!');
                    }
                }
            });
        } else {
            console.error('No cameras found.');
            alert('No cameras found.');
        }
    }).catch(function (e) {
        console.error(e);
        alert(e);
    });

});