#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/12/23 9:46 AM
# @Author  : zhangchao
# @File    : losses.py
# @Email   : zhangchao5@genomics.cn
import torch
import torch.nn as nn
import torch.nn.functional as F


def scale_mse(recon_x, x, alpha=0.):
    return F.mse_loss(alpha * (x - recon_x).mean(dim=1, keepdims=True) + recon_x, x)


def contrast_loss(feat1, feat2, tau=0.07, weight=1.):
    sim_matrix = torch.einsum("ik, jk -> ij", feat1, feat2) / torch.einsum(
        "i, j -> ij", feat1.norm(p=2, dim=1), feat2.norm(p=2, dim=1))
    label = torch.arange(sim_matrix.size(0), device=sim_matrix.device)
    loss = F.cross_entropy(sim_matrix / tau, label) * weight
    return loss


def trivial_entropy(feat, tau=0.07, weight=1.):
    prob_x = F.softmax(feat / tau, dim=1)
    p = (prob_x / prob_x.norm(p=1)).sum(0)
    loss = (p * torch.log(p + 1e-8)).sum() * weight
    return loss


def cross_instance_loss(feat1, feat2, tau=0.07, weight=1.):
    sim_matrix = torch.einsum("ik, jk -> ij", feat1, feat2) / torch.einsum(
        "i, j -> ij", feat1.norm(p=2, dim=1), feat2.norm(p=2, dim=1))
    entropy = torch.distributions.Categorical(logits=sim_matrix / tau).entropy().mean() * weight
    return entropy


def kl_loss(feat_x1, feat_x2, tau):
    return torch.nn.KLDivLoss()((feat_x1 / tau).log_softmax(1), (feat_x2 / tau).softmax(1))


class CrossInstLoss(nn.Module):
    def __init__(self):
        super(CrossInstLoss, self).__init__()

    def forward(self, feat1, feat2, tau=0.07, weight=1.):
        sim_matrix = torch.einsum("ik, jk -> ij", feat1, feat2) / torch.einsum(
            "i, j -> ij", feat1.norm(p=2, dim=1), feat2.norm(p=2, dim=1))
        entropy = torch.distributions.Categorical(logits=sim_matrix / tau).entropy().mean() * weight
        del sim_matrix
        return entropy


class ScaleMseLoss(nn.Module):
    def __init__(self):
        super(ScaleMseLoss, self).__init__()

    def forward(self, x, recon_x):
        return F.mse_loss((x - recon_x).mean(dim=1, keepdims=True) + recon_x, x)
        # return F.mse_loss(recon_x, x)


class ContrastLoss(nn.Module):
    def __init__(self):
        super(ContrastLoss, self).__init__()

    def forward(self, feat1, feat2, tau=0.07, weight=1.):
        sim_matrix = torch.einsum("ik, jk -> ij", feat1, feat2) / torch.einsum(
            "i, j -> ij", feat1.norm(p=2, dim=1), feat2.norm(p=2, dim=1))
        label = torch.arange(sim_matrix.size(0), device=sim_matrix.device)
        loss = F.cross_entropy(sim_matrix / tau, label) * weight
        del sim_matrix
        del label
        return loss
