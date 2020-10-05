import model
import torch
import torchvision.transforms as transforms
import torchvision


class Avatar_Generator_Model():
    """
    # Methods

    __init__(dict_model): initializer

    dict_model: layers required to perform face-to-image generation (e1, e_shared, d_shared, d2, denoiser)  

    generate(face_image, output_path=None): reutrn cartoon generated from given face image, saves it to output path if given 

    load_weights(weights_path): loads weights from given path
    """

    def __init__(self):
        self.e1 = model.Encoder()
        self.e_shared = model.Eshared(0.5)
        self.d_shared = model.Dshared()
        self.d2 = model.Decoder()
        self.denoiser = model.Denoiser()

    def generate(self, face_image, output_path=None):
        face = self.__extract_face(face_image)
        return self.__to_cartoon(face, output_path)

    def load_weights(self, weights_path='weights/'):
        self.e1.load_state_dict(torch.load(
            weights_path + 'e1.pth', map_location=lambda storage, loc: storage))
        self.e1.eval()
        self.e_shared.load_state_dict(
            torch.load(weights_path + 'e_shared.pth', map_location=lambda storage, loc: storage))
        self.e_shared.eval()
        self.d_shared.load_state_dict(
            torch.load(weights_path + 'd_shared.pth', map_location=lambda storage, loc: storage))
        self.d_shared.eval()
        self.d2.load_state_dict(torch.load(
            weights_path + 'd2.pth', map_location=lambda storage, loc: storage))
        self.d2.eval()
        self.denoiser.load_state_dict(
            torch.load(weights_path + 'denoiser.pth', map_location=lambda storage, loc: storage))
        self.denoiser.eval()

    def __extract_face(self, face_image):
        #import model
        # segment image
        # remove background
        # return face
        return face_image

    def __to_cartoon(self, face, output_path):
        transform = transforms.Compose(
            [transforms.Resize((64, 64)), transforms.ToTensor()])
        face = transform(face).float()
        x = torch.stack(32*[face])
        with torch.no_grad():
            output = self.e1(x)
            output = self.e_shared(output)
            output = self.d_shared(output)
            output = self.d2(output)
            output = self.denoiser(output)
        if output_path is not None:
            # save to path
            # fileName.jpg part of output_path
            torchvision.utils.save_image(tensor=output, fp=output_path)
        return torchvision.transforms.ToPILImage()(output[0])
