t = file.choose()
dataset = read.csv(t, header = T)
attach(dataset)
dd = cbind(price_usd, price_btc, total_supply, market_cap_usd, available_supply,
           usd_raised ,eth_price_launch, btc_price_launch ,ico_duration, month, day, country, output)

regressor1 = lm(formula = output ~ usd_raised)
summary(regressor1)
anova(regressor1)


regressor2 = lm(formula = output ~ico_duration)
summary(regressor2)
anova(regressor2)

regressor3 = lm(formula = output ~ usd_raised + ico_duration)
summary(regressor3)
anova(regressor3)


regressor4 = lm(formula = output ~ market_cap_usd)
summary(regressor4)
anova(regressor4)

regressor5 = lm(formula = output ~ available_supply)
summary(regressor5)
anova(regressor5)

regressor6 = lm(formula = output ~ market_cap_usd + available_supply)
summary(regressor6)
anova(regressor6)

dd1 =  cbind(price_usd, price_btc)
dd2 =  cbind(total_supply, available_supply)
dd3 =  cbind(market_cap_usd, usd_raised)
dd4 =  cbind(btc_price_launch, month)
dd5 =  cbind(usd_raised, ico_duration)
dd6 =  cbind(market_cap_usd, ico_duration)

M <- cor(dd)
library(corrplot)
corrplot.mixed(M)
corrplot(M, method="number")
col <- colorRampPalette(c("#BB4444", "#EE9988", "#FFFFFF", "#77AADD", "#4477AA"))
corrplot(M, method="color", col=col(200),  
         type="upper", order="hclust", 
         addCoef.col = "black", # Add coefficient of correlation
         tl.col="black", tl.srt=45, #Text label color and rotation
         # Combine with significance
         
         diag=F 
)

library(PerformanceAnalytics)
chart.Correlation(dd, histogram = TRUE, pch = 20)

