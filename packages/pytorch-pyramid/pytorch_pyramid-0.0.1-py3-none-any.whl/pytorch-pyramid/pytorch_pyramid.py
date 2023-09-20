import torch
import torch.nn as nn
import torch.nn.functional as F

class ImagePyramid(nn.Module):
    def __init__(self, kernel_size=5) -> None:
        super(ImagePyramid, self).__init__()
        self.conv_3in = nn.Conv2d(in_channels=3, out_channels=3, kernel_size=kernel_size, stride=1, padding=0, bias=False)
        self.conv_1in = nn.Conv2d(in_channels=1, out_channels=1, kernel_size=kernel_size, stride=1, padding=0, bias=False)
        self.kernel = self._gauss_kernel(kernel_size=kernel_size, channels=3)
        self.single_kernel = self._gauss_kernel(kernel_size=kernel_size, channels=1)
    
    def _gauss_kernel(self, kernel_size=5, channels=3):
        kernel = torch.tensor([[1., 4., 6., 4., 1],
                               [4., 16., 24., 16., 4.],
                               [6., 24., 36., 24., 6.],
                               [4., 16., 24., 16., 4.],
                               [1., 4., 6., 4., 1.]])
        kernel /= 256.
        kernel = kernel.repeat(channels, 1, 1, 1).cuda()
        return kernel
    
    def _downsample(self, x):
        return x[:, :, ::2, ::2]
    
    def _upsample(self, x):
        cc = torch.cat([x, torch.zeros(x.shape[0], x.shape[1], x.shape[2], x.shape[3], device=x.device)], dim=3)
        cc = cc.view(x.shape[0], x.shape[1], x.shape[2]*2, x.shape[3])
        cc = cc.permute(0,1,3,2)
        cc = torch.cat([cc, torch.zeros(x.shape[0], x.shape[1], x.shape[3], x.shape[2]*2, device=x.device)], dim=3)
        cc = cc.view(x.shape[0], x.shape[1], x.shape[3]*2, x.shape[2]*2)
        x_up = cc.permute(0,1,3,2)
        return 4 * self._conv_gauss(x_up)
    
    def _conv_gauss(self, img, channels=3):
        return self.conv_3in(F.pad(img, (2, 2, 2, 2), mode='reflect')) if channels == 3 else self.conv_1in(F.pad(img, (2, 2, 2, 2), mode='reflect'))
    
    def laplacian_recon(self, laplacian_pyramid, pyramid_level=5):
        recon = laplacian_pyramid[-1]
        for i in range(pyramid_level - 1, 0, -1):
            up = self._upsample(recon)
            recon = up + laplacian_pyramid[i - 1]
        return recon
    
    def forward(self, img, pyramid_levels=5, mode='all'):
        '''
        guass_pyramid_size: 512(input image), 256, 128, 64
        laplacian_pyramid_size: 512, 256, 128, 64(minist image)
        '''
        if mode == 'gauss':
            gauss_pyramid = []
            gauss_pyramid.append(img)
            for _ in range(pyramid_levels - 1):
                filtered = self._conv_gauss(img, channels=img.shape[1])
                down = self._downsample(filtered)
                gauss_pyramid.append(down)
                img = down
            return gauss_pyramid
        elif mode == 'laplacian':
            lap_pyramid = []
            for _ in range(pyramid_levels - 1):
                filtered = self._conv_gauss(img, channels=img.shape[1])
                down = self._downsample(filtered)
                up = self._upsample(down)
                diff = img - up
                lap_pyramid.append(diff)
                img = down
            lap_pyramid.append(img)
            return lap_pyramid
        elif mode == 'all':
            gauss_pyramid = []
            lap_pyramid = []
            gauss_pyramid.append(img)
            for _ in range(pyramid_levels - 1):
                filtered = self._conv_gauss(img, channels=img.shape[1])
                down = self._downsample(filtered)
                up = self._upsample(down)
                diff = img - up
                gauss_pyramid.append(down)
                lap_pyramid.append(diff)
                img = down
            lap_pyramid.append(img)
            return gauss_pyramid, lap_pyramid
        else:
            assert False, 'mode must be gauss, laplacian or all'